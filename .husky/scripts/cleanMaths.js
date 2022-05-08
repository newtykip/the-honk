const fs = require('fs');
const path = require('path');
const { pdfToPng } = require('pdf-to-png-converter');
const Jimp = require('jimp');

const mathsDir = path.resolve(__dirname, '..', '..', 'maths');

const cropBuffer = buffer =>
    new Promise((resolve, reject) => {
        Jimp.read(buffer)
            .then(cropped => {
                cropped.autocrop();

                new Jimp(
                    cropped.getWidth() + 100,
                    cropped.getHeight() + 100,
                    '#ffffff',
                    async (err, image) => {
                        if (err) reject(err);

                        image.blit(cropped, 50, 50);

                        resolve(await image.getBufferAsync(Jimp.MIME_PNG));
                    }
                );
            })
            .catch(err => reject(err));
    });

const crawlDirectory = async dir => {
    const dirents = fs.readdirSync(dir, { withFileTypes: true });

    const files = await Promise.all(
        dirents.map(dirent => {
            const res = path.resolve(dir, dirent.name);
            return dirent.isDirectory() ? crawlDirectory(res) : res;
        })
    );

    return files.flat();
};

(async () => {
    const files = await crawlDirectory(mathsDir);

    files.forEach(file => {
        const [filePath, fileDirectory, fileNameWithExt] = file.match(/(.*)\/((?:.(?!\/))+)$/);
        const [fileName, fileExtension] = fileNameWithExt.split('.');

        if (file.endsWith('.pdf')) {
            pdfToPng(filePath).then(async output => {
                const pageCount = output.length;

                if (pageCount > 1)
                    output.forEach(async (page, i) =>
                        fs.writeFileSync(
                            path.join(fileDirectory, `${fileName}-${i + 1}.png`),
                            await cropBuffer(page.content)
                        )
                    );
                else
                    fs.writeFileSync(
                        path.join(fileDirectory, `${fileName}.png`),
                        await cropBuffer(output[0].content)
                    );
            });
        }

        if (fileExtension !== 'tex' && fileExtension !== 'png' && fileExtension !== 'cls') {
            fs.rmSync(filePath);
        }
    });
})();

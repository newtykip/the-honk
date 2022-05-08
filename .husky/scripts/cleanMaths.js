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

fs.readdirSync(mathsDir).forEach(file => {
    const [fileName, fileExtension] = file.split('.');
    const filePath = path.join(mathsDir, file);

    if (file.endsWith('.pdf')) {
        pdfToPng(filePath, {
            viewportScale: 2
        }).then(async output => {
            const pageCount = output.length;

            if (pageCount > 1)
                output.forEach(async (page, i) =>
                    fs.writeFileSync(
                        path.join(mathsDir, `${fileName}-${i + 1}.png`),
                        await cropBuffer(page.content)
                    )
                );
            else
                fs.writeFileSync(
                    path.join(mathsDir, `${fileName}.png`),
                    await cropBuffer(output[0].content)
                );
        });
    }

    if (fileExtension !== 'tex' && fileExtension !== 'png' && fileExtension !== 'cls') {
        fs.rmSync(filePath);
    }
});

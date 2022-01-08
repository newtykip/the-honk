const fs = require('fs');
const chalk = require('chalk');
const { spawnSync } = require('child_process');
const perf = require('execution-time')();

const generateBanner = text => {
    // Calculate the length of the divider
    let divider = '--';

    for (let j = 0; j < text.length; j++) {
        divider += '-';
    }

    return `${divider}
${chalk.bold(chalk.greenBright(text))}
${divider}`;
};

const run = file => {
    console.log(generateBanner(file.split('.ts')[0]));

    // Execute the file
    perf.start();
    spawnSync('npx', ['ts-node', `"src/${file}"`], {
        shell: true,
        stdio: 'inherit'
    });
    const results = perf.stop();

    // Print time results
    console.log();
    console.log(chalk.bold(chalk.yellow(`Executed in ${results.words}`)));
};

// Get files
const tsFiles = fs
    .readdirSync('src')
    .filter(f => f.endsWith('.ts'))
    .filter(f => f !== 'utils.ts');

// Extract the puzzle number
const puzzleNumber = process.argv[2];

if (puzzleNumber === 'all' || !puzzleNumber) {
    tsFiles
        .sort((a, b) => {
            a = parseInt(a.split('-')[0]);
            b = parseInt(b.split('-')[0]);

            return a > b ? 1 : -1;
        })
        .forEach(file => {
            run(file);
            console.log();
        });
} else if (!isNaN(puzzleNumber)) {
    // Find the associated puzzle
    const [file] = tsFiles.filter(f => f.startsWith(puzzleNumber));
    run(file);
} else {
    console.log(
        chalk.bold(
            chalk.red('Please ensure that you input the number of the puzzle to run - thank you.')
        )
    );
}

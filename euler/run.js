const fs = require('fs');
const chalk = require('chalk');
const { spawnSync } = require('child_process');

const run = (file, puzzleName) => {
    // Calculate the length of the divider for the puzzle
    let divider = '--';

    for (let j = 0; j < puzzleName.length; j++) {
        divider += '-';
    }

    // Log output
    console.log(divider);
    console.log(chalk.bold(chalk.greenBright(puzzleName)));
    console.log(divider);

    spawnSync('node', [`build/${file}`], { shell: true, stdio: 'inherit' });
};

// Get files
const tsFiles = fs
    .readdirSync('src')
    .filter(f => f.endsWith('.ts'))
    .filter(f => f !== 'utils.ts');
const jsFiles = fs
    .readdirSync('build')
    .filter(f => f.endsWith('.js'))
    .filter(f => f !== 'utils.js');

try {
    // Extract the puzzle number
    const puzzleNumber = process.argv[2];
    if (isNaN(puzzleNumber)) throw Error();

    // Find the associated puzzle
    const tsFile = tsFiles.filter(f => f.startsWith(puzzleNumber))[0];
    const puzzleName = tsFile.split('.ts')[0];

    run(`${puzzleNumber}.js`, puzzleName);
} catch (error) {
    for (let i = 0; i < jsFiles.length; i++) {
        const file = jsFiles[i];
        const tsFile = tsFiles[i];
        const puzzleName = tsFile.split('.ts')[0];

        run(file, puzzleName);
        console.log();
    }
}

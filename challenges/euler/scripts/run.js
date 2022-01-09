const fs = require('fs');
const chalk = require('chalk');
const { spawnSync } = require('child_process');
const executionTime = require('execution-time')();
const ms = require('ms');

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
    executionTime.start();

    spawnSync('npx', ['ts-node', `"src/${file}"`], {
        shell: true,
        stdio: 'inherit'
    });

    const results = executionTime.stop();

    // Print time results
    console.log();
    console.log(chalk.bold(chalk.yellow(`Executed in ${results.words}`)));

    return results.time;
};

const runMany = files => {
    let totalTime = 0;

    files.forEach(file => {
        const time = run(file);
        totalTime += time;
        console.log();
    });

    console.log(
        chalk.magenta(
            chalk.bold(
                `This set of executions took roughly ${ms(totalTime, { long: true })} in total!`
            )
        )
    );
};

// Get files
const allFiles = fs
    .readdirSync('src')
    .filter(f => f.endsWith('.ts'))
    .filter(f => f !== 'utils.ts');

// Extract the puzzle number
process.argv.shift();
process.argv.shift();

if (process.argv[0] === 'all' || process.argv.length === 0) {
    const files = allFiles.sort((a, b) => {
        a = parseInt(a.split('-')[0]);
        b = parseInt(b.split('-')[0]);

        return a > b ? 1 : -1;
    });

    runMany(files);
} else if (process.argv.length > 1 || process.argv[0].includes(',')) {
    let puzzleNumbers = process.argv
        .map(v =>
            v.includes(',')
                ? v.split(',').map(e => (!isNaN(e) ? parseInt(e) : null))
                : !isNaN(v)
                ? parseInt(v)
                : null
        )
        .flat()
        .filter(e => e !== null);
    puzzleNumbers = puzzleNumbers.filter((e, i) => puzzleNumbers.indexOf(e) === i);

    const files = allFiles.filter(f =>
        f.match(
            `^(?:[${puzzleNumbers.map((number, i) =>
                i === puzzleNumbers.length - 1 ? number : `${number}|`
            )}]) -`
        )
    );

    runMany(files);
} else if (!isNaN(process.argv[0])) {
    // Find the associated puzzle
    const [file] = allFiles.filter(f => f.startsWith(process.argv[0]));
    run(file);
} else {
    console.log(
        chalk.bold(
            chalk.red('Please ensure that you input the number of the puzzle to run - thank you.')
        )
    );
}

// You are given the following information, but you may prefer to do some research for yourself.
// 1 Jan 1900 was a Monday.
// Thirty days has September,
// April, June and November.
// All the rest have thirty-one,
// Saving February alone,
// Which has twenty-eight, rain or shine.
// And on leap years, twenty-nine.
// A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
// How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
export = {};

interface Date {
    year: number;
    month: number;
    date: number;
}

/**
 * Find all of the Sundays in a given
 */
const sundaysInAYear = (year: number): Date[] => {
    const time = new Date(year, 0, 1);

    while (time.getDay() != 0) {
        time.setDate(time.getDate() + 1);
    }

    const dates = [];

    while (time.getFullYear() === year) {
        const month = time.getMonth() + 1;
        const date = time.getDate();

        dates.push({
            year,
            month,
            date
        });

        time.setDate(time.getDate() + 7);
    }

    return dates;
};

// Output
let dates: Date[] = [];

for (let year = 1901; year <= 2000; year++) {
    dates = [...dates, ...sundaysInAYear(year)];
}

let count = 0;

dates.forEach(({ date }) => {
    if (date == 1) {
        count += 1;
    }
});

console.log(count);

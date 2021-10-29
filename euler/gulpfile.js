const gulp = require('gulp');
const typescript = require('gulp-typescript');
const uglify = require('gulp-uglify');
const rename = require('gulp-rename');

gulp.task('build', () => {
    const tsc = typescript.createProject('tsconfig.json');

    return gulp
        .src('src/**/*.ts')
        .pipe(tsc())
        .pipe(uglify({ mangle: { toplevel: true } }))
        .pipe(
            rename(path => {
                if (path.basename === 'utils') return;
                path.basename = path.basename.split('-')[0].trim();
            })
        )
        .pipe(gulp.dest('build'));
});

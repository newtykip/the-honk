#!/bin/bash
find . -print0 | while IFS= read -r -d '' file
do
  if [ -f "$file" ]; then
	if [[ $file == *pdf ]]; then
		mkdir temp
		gm convert "$file" +adjoin temp/temp%02d.png

		for temp in ./temp/*.png
		do
			gm convert "$temp" -fuzz 80% -trim +repage -bordercolor white -border 50x25 "$temp"
		done

		readarray -d . -t arr <<< $file

		gm convert -append ./temp/*.png "${arr[1]:1}.png"
		
		rm -rf temp
		rm "$file" "${arr[1]:1}.synctex.gz"
	fi
fi
done

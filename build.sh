hex=$(openssl rand -hex 2)

mkdir -p build
cp $1 build/main.py
cd build || exit
flet publish main.py --distpath "../r/$2-$hex" --base-url "r/$2-$hex" --app-name "$2"
git add "../r/$2-$hex"
git commit -m "Add result files for $2-$hex."
echo "https://s.nekstas.ru/r/$2-$hex"

pytest test_main.py > resultest.txt
if [[ $? == 0 ]]; then
  git add main.py fizzbuzz.py views/
  git commit -m "tests ok"
  git push origin main
  echo "tout va bien!"
else
  echo "les tests passent pas"
  tail -n 50 resultest.txt
fi

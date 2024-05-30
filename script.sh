echo "lancement des test..."
pytest test_main.py > resultest.txt
if [[ $? == 0 ]]; then
  echo "git add..."
  git add main.py fizzbuzz.py views/
  echo "git commit..."
  git commit -m "tests ok"
  echo "git push"
  git push origin main
  echo "tout va bien!"
else
  echo "les tests passent pas"
  tail -n 50 resultest.txt
fi

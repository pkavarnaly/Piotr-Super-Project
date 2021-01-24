rem chrome
pytest -v -s -m "sanity" --html=./Reports/report_chrome.html testCases/ --browser chrome
rem pytest -v -s -m "sanity or regression" --html=./Reports/report_chrome.html testCases/ --browser chrome
rem pytest -v -s -m "sanity and regression" --html=./Reports/report_chrome.html testCases/ --browser chrome
rem pytest -v -s -m "regression" --html=./Reports/report_chrome.html testCases/ --browser chrome


rem firefox
rem pytest -v -s -m "sanity" --html=./Reports/report_firefox.html testCases/ --browser firefox
rem pytest -v -s -m "sanity or regression" --html=./Reports/report_firefox.html testCases/ --browser firefox
rem pytest -v -s -m "sanity and regression" --html=./Reports/report_firefox.html testCases/ --browser firefox
rem pytest -v -s -m "regression" --html=./Reports/report_firefox.html testCases/ --browser firefox
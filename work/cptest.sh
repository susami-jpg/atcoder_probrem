
#!/bin/bash

problem_name=$1
test_dir=test/${problem_name}
base_url=${problem_name%_*}

rem # log in
oj login -u hasami889 -p Saskazu330 "https://atcoder.jp/"
oj login --check "https://atcoder.jp/"

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d test/${problem_name} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
fi

oj test -c "python3 problems/${problem_name}.py" -d test/${problem_name}


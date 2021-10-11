!#/usr/bin/env bash

set -ux

TF_DIR=/root/tensorflow-upstream
RUN_TEST_PATH=/root/scripts/run_test.sh

cd $TF_DIR

main(){
    # the commit id that does not fail
    local left_comm_id=7e8f960bb398526aea7e045884101029fd21bddd

    # the commit id that fails
    local right_comm_id=7f185962b837844e88168bc2aad364a9e599292c

    local test_name=//tensorflow/compiler/tests:randomized_tests_seeded_gpu

    git clean -f -d
    git checkout $right_comm_id
    comm_count=$(find_number_of_commits $left_comm_id $right_comm_id)
    echo "initial commit counts are "${comm_count} >&2

    while [ $comm_count -gt 0 ]
    do
        git clean -f -d
        git checkout $right_comm_id
        git clean -f -d

        if [ $comm_count -gt 1 ]
        then
            git checkout HEAD~$((comm_count / 2))
        else
            git checkout HEAD~1
        fi
        mid_id=$(git rev-parse HEAD)

        $RUN_TEST_PATH $test_name
        code=$?
        echo "return code is ${code}" >&2

        if [ "$code" -eq "0" ]
        then
            echo "taking right" >&2
            left_comm_id=$mid_id
        else
            echo "taking left" >&2
            right_comm_id=$mid_id
        fi
        comm_count=$(find_number_of_commits $left_comm_id $right_comm_id)
        echo "new commit counts are "${comm_count} >&2
    done
    
    echo "left=${left_comm_id}, right=${right_comm_id}"
}

find_number_of_commits()
{
    # find the number of commits between $1 and $2 (excluding $1 and $2)
    local l=$1
    local r=$2
    count=$(git rev-list --count --first-parent $l..$r)
    echo $((count - 1))
}

result=$(main "$@")

echo "Answer: ${result}"


exit


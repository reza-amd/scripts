echo "Find the id of the docker exec process"
echo "    ps -ef | grep \"docker exec -ti <containter_name> bash\" "
echo "and then send it the SIGWINCH signal"
echo "    kill -SIGWINCH <process_id>"

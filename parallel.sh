#!/bin/bash
for cmd in "$@"; do {
  echo "Process \"$cmd\" started";
  $cmd & pid=$!
  PID_LIST+=" $pid";
} done
trap "kill -- -$(ps -o pgid= $$ | grep -o '[0-9]*')" SIGINT
wait $PID_LIST
echo "All Process closed"
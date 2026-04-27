#!/bin/bash

# Fetch memory
fetch_memory() {
	total_mem=$(free | awk '/Mem:/ { print $2}')
	# total_mem=0
	avail_mem=$(free | awk '/Mem:/ { print $7}')
	# avail_mem='test'

	if [[ -z "$total_mem" || -z "$avail_mem" || "$total_mem" -eq 0 || "$avail_mem" -eq 0 ]]; then
		return 1
	 fi

	 mem_percentage=$(( ($total_mem - $avail_mem) * 100 / $total_mem))

	 echo "Memory Utilization - $mem_percentage% (Available: ~$(($avail_mem/1024/1024))GB)"
}


if ! fetch_memory; then
	echo "Memory Utilization: Issue with fetching the memory"
fi

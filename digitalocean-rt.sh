# Digital Ocean Ping Time

for DC in nyc1 nyc2 nyc3 ams2 ams3 sfo1 sfo2 sgp1 lon1 fra1 tor1 blr1; do echo "$DC: $(ping -i .2 -c 75 -q speedtest-$DC.digitalocean.com | awk -F/ '/^round|^rtt/{print $5}')"; done | sort -n -k2
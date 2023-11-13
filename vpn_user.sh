#! /bin/bash

# 1. Ask VPN username and ID
echo ""
read -p "Username : " username
read -p "ID : " id
echo ""

# 2. Create folder, private and public keys
mkdir $username
wg genkey | tee $username-private.key | wg pubkey > $username-public.key

# 3.1 User configuration file
echo "[Interface]" > $username.conf
printf -v user_prikey 'PrivateKey = %s' "$(<$username-private.key)"
echo $user_prikey >> $username.conf
printf -v user_addr 'Address = 10.8.0.%s/32, fd08::%s/128' "$id" "$id"
echo $user_addr >> $username.conf
echo 'DNS = 1.1.1.1, 2606:4700:4700::64

[Peer]
PublicKey = 9jms30rGvtahLJ3ZN3bbFiW6a1QUfZ7lKTBT4k0HEWA=
AllowedIPs = 0.0.0.0/0, ::/0
Endpoint = 167.71.65.252:51820' >> $username.conf

# 3.2 Server configuration file
echo '
[Peer]' > server.conf
printf -v user_pubkey 'PublicKey = %s' "$(<$username-public.key)"
echo $user_pubkey >> server.conf
printf -v user_ip 'AllowedIPs = 10.8.0.%s/32, fd08::%s/128' "$id" "$id"
echo $user_ip >> server.conf
# echo 'Endpoint = 0.0.0.0:0' >> server.conf

# 4 Move files to user directory
mv $username-private.key $username-public.key $username.conf server.conf -t $username/

# 5. Add user to wireguard 
cat $username/server.conf >> /etc/wireguard/wg0.conf
wg syncconf wg0 <(wg-quick strip wg0)

# 6. Show user QR Code
echo ""
qrencode -t ansiutf8 < $username/$username.conf
echo ""

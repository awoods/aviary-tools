#!/bin/bash

source .creds

f=.env
t=.tmp

rm $f
curl -v -X POST https://hlavmass.lib.harvard.edu/api/v1/auth/sign_in -F email=${USERNAME} -F password=${PASSWORD} -D $t
clear
grep 'uid\|client\|access-token' $t | sed -e 's/\([a-z|-]*\): \(.*\)/\1=\2/' > $f
rm $t

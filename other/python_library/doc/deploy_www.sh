#!/bin/bash
# Script to rsync the local directory with the wiliki remote web server

# This will require a password
#rsync -arzv ./www/ bsb@wiliki.eng.hawaii.edu:./Html/me402/

# After setting up a public/private key
# http://www.thegeekstuff.com/2008/11/3-steps-to-perform-ssh-login-without-password-using-ssh-keygen-ssh-copy-id/
# Now this does not require a password!
rsync -arzv ./_build/html/ 'wiliki.eng.hawaii.edu':./Html/me492_696/pici/
echo "All done - close in 2 s"
sleep 2
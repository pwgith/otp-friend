# For this to be called from serverless you have to install script plugins:
#    npm install --save serverless-plugin-scripts
#    serverless plugin install -n serverless-plugin-scripts
# And add the following to the serverless yml file:
# custom:
#   scripts:
#     hooks:
#       'deploy:finalize': karate/refresh_urls.sh

serverless info --verbose | grep -e POST -e GET -e PATCH > karate/all_urls.txt
grep "POST.*otp$" karate/all_urls.txt  | sed -n 's/^.* - //p' | tr -d '\n' > karate/url_otp_post.txt
grep "POST.*otp_okta$" karate/all_urls.txt  | sed -n 's/^.* - //p' | tr -d '\n' > karate/url_otp_okta_post.txt
grep "POST.*otp$" karate/all_urls.txt   | sed -n 's/^.* - //p' | tr -d '\n' > karate/url_otp_get.txt
# Note the get url is re-using the post url, this is because the post and get urls are the same except the get
# has a key on the end, so reusing the post is less work

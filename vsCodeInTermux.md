
pkg update -y
pkg install -y python nodejs yarn git
yarn global add code-server



pkg install binutils;
v=$(node -v); v=${v#v}; v=${v%%.*};
FORCE_NODE_VERSION="$v" yarn global add code-server --ignore-engines;
code-server;


Not Finished

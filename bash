# Setting PATH for Python 2.7
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/2.7/bin:${PATH}"
export PATH

# Setting PATH for elsa
export PATH="/Users/liguangyao/.local/bin:$PATH"

alias ls="ls -G"
alias ks="ls"
alias ll="ls -l"
alias la="ls -a"
alias lg="ssh gli38@unix.ucsc.edu"
alias cld="cd ~/Calendar/; git pull; cd; python Calendar/c.py; cd Calendar/; upload; cd"
alias voc="cd ~/Vocabulary; git pull; python sql.py; upload; cd"
alias download="youtube-dl -f bestvideo+bestaudio"
alias downloadmp3="youtube-dl --extract-audio --audio-format mp3"
alias sek='f(){ find / -name $1; }; f'
alias hsc='f(){ ghc -o $1 $1.hs; echo deleting $1.o $1.hi; rm *.o *.hi; }; f'
alias VtoA="ffmpeg -i $1 -f mp3 -ab 192000 -vn $2"
alias rconnect="ssh liguangyao@10.0.0.19"
alias ChinaConnect="ssh liguangyao@58.247.95.138"
alias dic="sdcv"
alias dict="sdcv"
alias weather='f(){ curl wttr.in/$1?m; }; f'
alias oepn='open'
alias ubuntu='docker run -it awesome_linux'
alias CSE120_S='ssh cse120_16@bohr1.soe.ucsc.edu'
alias shfs='sshfs gli38@unix.ucsc.edu:/afs/cats.ucsc.edu/users/p/gli38 ~/TimeShare/'
alias pyIns='python3 -O -m PyInstaller'
alias gw='say -v Sin-ji -f ~/CS/rubbish/good_words.txt -r 205'
alias dj='cd CLI-Piano; ./piano'
alias pyton3='python3'
alias pyton='python'

# git
alias update="git pull; git add ./*; git commit -m \"auto-update by my python script\"; git push"
alias upload="git add ./*; git commit -m \"auto-update by my python script\"; git push"
alias gpull='git pull'
alias gadd='git add'
alias gcm='git commit -m'
alias gpush='git push'

# Quick access to open some frequently used websites
alias Google='open http://www.google.com'
alias Youtube='open https://www.youtube.com'
alias Map='open https://www.google.com/maps'
alias UCSC='open https://www.ucsc.edu'
alias MyUCSC='open https://my.ucsc.edu'
alias Canvas='open https://canvas.ucsc.edu'
alias CS112='open https://users.soe.ucsc.edu/~owen/courses/cmps112/spr19/index.html'
alias Gitlab='open https://gitlab.soe.ucsc.edu/gitlab'
alias Github='open https://github.com'
alias RMP='open https://www.ratemyprofessors.com'
alias RateMyProfessor='open https://www.ratemyprofessors.com'
alias iq='f(){ open http://tiny.cc/cse116-$1-ind; }; f'
alias gq='f(){ open http://tiny.cc/cse116-$1-grp; }; f'
alias hackerMode="open http://thepierealm.coffeecup.com/hackerTyper/index.html"
alias Bing="open https://www.bing.com/"

export PATH="/usr/local/sbin:$PATH"
source /Users/liguangyao/.ghcup/env
export CPLUS_INCLUDE_PATH=/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/include/python3.7m
export C_INCLUDE_PATH=/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/include/python3.7m
export PATH="/usr/local/opt/libxml2/bin:$PATH"
export http_proxy='http://localhost:8118'
export https_proxy='http://localhost:8118'

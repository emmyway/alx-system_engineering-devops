#!/usr/bin/env ruby
sender =  ARGV[0].scan(/from:\+?\w*/).join[5..-1]
receiver = ARGV[0].scan(/to:\+?\w*/).join[3..-1]
flags = ARGV[0].scan(/flags:(.*?)]/).join
msg = sender + "," + receiver + "," + flags
puts msg

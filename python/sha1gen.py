#!/usr/bin/env python3

# Get SHA-1 hex string

import sha

s = 'String to Convert'
print(sha.new(s).hexdigest())

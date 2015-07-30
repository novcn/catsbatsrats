Cats Bats Rats
===================
Demo using streamparse to allow a bolt to dynamically choose an emit target. The bolt "hash-bolt" has logic to determine which of the three subscribed bolts to emit to.

There are three components which allow this to work:

Output specification (topologies/*.clj) for a bolt or spout, see
[Clojure-DSL](http://storm.apache.org/documentation/Clojure-DSL.html)
for more info
``` ;; streamid ["tuple_key"], the "Cats" bolt will subscribe to the stream of id "c" and so on.
   {"c" ["demon"]
   "b" ["demon"]
   "r" ["demon"]}
```

Code choosing which streamid to emit to (src/bolts/*.py |
src/spouts/*.py)
```
  streamid = #some computation
  self.emit(["tuples"], stream=streamid) 
```

Input specification (topologies/*.clj)
```
  ;subscribe Cats bolt to hash-bolt with streamid "c"
  {["hash-bolt" "c"] :shuffle}
```

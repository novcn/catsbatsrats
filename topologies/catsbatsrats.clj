(ns catsbatsrats
  (:use     [streamparse.specs])
  (:gen-class))

(defn catsbatsrats [options]
   [
    ;; spout configuration
    {"number-spout" (python-spout-spec
          options
          "spouts.numbers.NumberSpout" ;; name of python class to run
          ["number"] ;; output specification
          :p 4)
    }
    ;; bolt configuration
    {
     "hash-bolt" (python-bolt-spec
          options
          {"number-spout" :shuffle} ;; receives tuples from number-spout
          "bolts.hash.HashTable" ;; python class to run
          ;; output specification
          {"c" ["word"] ;streamid ["tuple key"]
           "b" ["word"]
           "r" ["word"]}
          :p 4
          )
     "cat-bolt" (python-bolt-spec
          options
          {["hash-bolt" "c"] :shuffle} ;subscribe to hash-bolt @ id c
          "bolts.demons.Cats" ;fire Cats bolt
          ["demon"] ; output specification, not used
          :p 4
          )
     "bat-bolt" (python-bolt-spec
          options
          {["hash-bolt" "b"] :shuffle}
          "bolts.demons.Bats"
          ["demon"]
          :p 4
          )
     "rat-bolt" (python-bolt-spec
          options
          {["hash-bolt" "r"] :shuffle}
          "bolts.demons.Rats"
          ["demon"]
          :p 4
          )
    }
 ]
)

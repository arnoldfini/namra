'''{
  outer1:{
    inner1:{
      "a":1,
      "b":2,
      "c":4,
    },
    inner2:{
      "a":5,
      "b":7,
      "c":9,
    },
    }
  outer2:{
     inner1:{
      "a":6,
      "b":5,
      "c":1,
    },
    inner2:{
      "a":5,
      "b":8,
      "c":12,
    },

  }
}'''
header=["a","b","c"]
list=[1,2,4,5,7,9,6,5,1,5,8,12]
inner = ['inner1', 'inner2']

subdict = {key for key in inner}
subsubdict = {key: value for key in header and list}
print(subsubdict)
#dict = {subdict{subsubdict}}
print(sum(int(l[0] + l[-1]) for l in map(lambda x: [i for i in x if i.isdigit()], map(lambda x: x.replace("twone", "twoone").replace("oneight", "oneeight").replace("threeight", "threeeight").replace("fiveight", "fiveeight").replace("nineight", "nineeight").replace("sevenine", "sevennine").replace("eightwo", "eighttwo").replace("one", '1').replace("two", '2').replace("three", '3').replace("four", '4').replace("five", '5').replace("six", '6').replace("seven", '7').replace("eight", '8').replace("nine", '9'), open("input.txt")))))

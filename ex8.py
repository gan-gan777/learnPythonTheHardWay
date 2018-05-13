# -*- coding:UTF-8 -*-

formatter = "%s %s %s %s"

print formatter % ("你好", "好嘞", "怎么样", "嗨")
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)
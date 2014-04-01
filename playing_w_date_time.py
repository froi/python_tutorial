from datetime import datetime

def print_date_parts():
	now = datetime.now()

	print '\tNow: %s' % now
	print '\tYear: %d' % now.year
	print '\tMonth: %d' % now.month
	print '\tDay: %d' % now.day
	print '\tHour: %d' % now.hour
	print '\tMinute: %d' % now.minute
	print '\tSecond: %d' % now.second

def print_date():
	now = datetime.now()

	print '\tFormatting our datetime to MM/DD/YYYY'

	print '\t' + str(now.month) + "/" + str(now.day) + "/" + str(now.year)
	print '\t%d/%d/%d' % (now.month, now.day, now.year)

def print_date_time():
	now = datetime.now()

	print '\tFormatting our datetime to MM/DD/YYYY hh:mm:ss'

	print '\t' + str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
	print "\t%d/%d/%d %d:%d:%d" % (now.month, now.day, now.year, now.hour, now.minute, now.second)
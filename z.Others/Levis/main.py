from bbc_parsing import bbc_links_parse

file = open("bbc_stories.txt", "w")
stories = bbc_links_parse()
for line_of_stories in stories:
    file.write(line_of_stories.encode("utf8"))
file.close()

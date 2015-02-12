
import re
import os


def get_markdown_files(summary_file):
    pattern = re.compile('.*?\((ch\d+\S+)\)')

    with open(summary_file) as f:
        for line in f:
            m = pattern.match(line)

            if m:
                filename = m.group(1)
                if not os.path.exists(filename.replace('.md', '.py')):
                    raise FileNotFoundError(filename)

                yield filename



for md_file_name in list(get_markdown_files('./SUMMARY.md')):
    py_file_name = md_file_name.replace('.md', '.py')

    code_segment_prefix = '```python'
    code_segment_suffix = '```'
    new_line = '\n'
    # this grammar only works on python 3,
    # contextlib.nested can be used on python 2
    with open(py_file_name) as py_file, open(md_file_name, 'wt') as md_file:
        segment = 'undefined'

        for py_line in py_file:
            py_line = py_line.rstrip()
            # if it's empty line
            if not py_line:
                md_file.write(py_line)
                md_file.write(new_line)

            elif py_line.startswith('#'):
                if segment == 'code':
                    md_file.write(code_segment_suffix)
                    md_file.write(new_line)
                    md_file.write(new_line)

                segment = 'comment'

                md_file.write(py_line.lstrip('#'))
                md_file.write(new_line)
            else:
                if segment != 'code':
                    md_file.write(code_segment_prefix)
                    md_file.write(new_line)

                segment = 'code'

                md_file.write(py_line)
                md_file.write(new_line)



        if segment == 'code':
            md_file.write(code_segment_suffix)
            md_file.write(new_line)
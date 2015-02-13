
import re
import os


def get_markdown_files(summary_file):
    pattern = re.compile('.*?\((ch\d+\S+)\)')

    with open(summary_file) as f:
        for line in f:
            m = pattern.match(line)

            # if there is a .md file specified
            if m:
                filename = m.group(1)
                # if the file is not end with .md,
                # then it should be a spell mistake
                if not filename.endswith('.md'):
                    raise SyntaxError(filename + ' should be a .md file')

                # the python file should exist
                # other wise it can not generate .md from .py
                if not os.path.exists(filename.replace('.md', '.py')):
                    raise FileNotFoundError(filename)

                yield filename


def generate_markdown(source_file_extension='.py',
                      code_segment_prefix = '```python',
                      code_segment_suffix = '```',
                      new_line = '\n',
                      summary_file='./SUMMARY.md'):
    for md_file_name in list(get_markdown_files(summary_file)):
        source_file_name = md_file_name.replace('.md', source_file_extension)


        with open(source_file_name) as py_file, open(md_file_name, 'wt') as md_file:
            segment = 'undefined'

            for py_line in py_file:
                py_line = py_line.rstrip()
                # if it's empty line
                # then we just add the empty line
                # but don't change the segment type
                if not py_line:
                    md_file.write(new_line)

                # if it's a comment one top level (no indention)
                elif py_line.startswith('#'):
                    # if it was code previously, then we need end the code segment
                    if segment == 'code':
                        md_file.write(code_segment_suffix)
                        md_file.write(new_line)
                        md_file.write(new_line)

                    # now the segment becomes comment
                    segment = 'comment'

                    # we remove the first two characters '# '
                    # the consequence string can be anything valid for markdown
                    md_file.write(py_line.lstrip('# '))
                    md_file.write(new_line)
                else:
                    # if it's a start of code segment
                    # then we add a prefix
                    if segment != 'code':
                        md_file.write(code_segment_prefix)
                        md_file.write(new_line)

                    # now it's code
                    segment = 'code'

                    # add the line back
                    md_file.write(py_line)
                    md_file.write(new_line)

            # after the whole file is processed
            # if the previous segment is code, then we need end the code segment
            if segment == 'code':
                md_file.write(code_segment_suffix)
                md_file.write(new_line)


if __name__ == '__main__':
    # can be extended to handle other source files
    generate_markdown()
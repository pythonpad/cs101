import hashlib
import json
import os
import pathlib
import re
import shutil

BUILD_PATH = os.path.join(pathlib.Path().absolute(), 'build')
COURSE_PATH = os.path.join(pathlib.Path().absolute(), 'pypad-courses')

def generate_hash_for_pad(file_path):
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_sha256.update(chunk)
    hex_string = hash_sha256.hexdigest()
    with open(file_path + '.hash', 'w') as f:
        f.write(hex_string)

def init_target_path():
    if os.path.exists(BUILD_PATH):
        shutil.rmtree(BUILD_PATH)
    os.makedirs(BUILD_PATH)

def get_course_ids():
    course_ids = os.listdir(COURSE_PATH)
    return course_ids

def replace_paths(body, course_id):
    text = body
    text = re.sub(r'src="\.\.\/assets\/([^"]*)"', lambda m: 'src="/static/courses/%s"' % os.path.join(course_id, m.group(1)), text)
    text = re.sub(r'!\[([^\]]*)\]\(\.\.\/assets\/([^)]*)\)', lambda m: '![%s](/static/courses/%s)' % (m.group(1), os.path.join(course_id, m.group(2))), text)
    text = re.sub(r'src="\.\.\/pads\/([^"]*)"', lambda m: 'src="../../pads/%s"' % os.path.join(course_id, m.group(1)), text)
    return text

def build_table(course_id):
    table_source_path = os.path.join(COURSE_PATH, course_id, 'course.json')
    with open(table_source_path, 'r') as f:
        table_text = f.read()
    
    tables_build_path = os.path.join(BUILD_PATH, 'tables')
    if not os.path.exists(tables_build_path):
        os.makedirs(tables_build_path)
    table_target_path = os.path.join(tables_build_path, '%s.json' % course_id)
    with open(table_target_path, 'w') as f:
        f.write(table_text)

def build_docs(course_id):
    docs_source_path = os.path.join(COURSE_PATH, course_id, 'docs')
    doc_filenames = [filename for filename in os.listdir(docs_source_path) if filename.endswith('.md')]

    docs_build_path = os.path.join(BUILD_PATH, 'docs', course_id)
    if not os.path.exists(docs_build_path):
        os.makedirs(docs_build_path)

    for doc_filename in doc_filenames:
        with open(os.path.join(docs_source_path, doc_filename), 'r') as f:
            doc_body = f.read()
        with open(os.path.join(docs_build_path, doc_filename), 'w') as f:
            f.write(replace_paths(doc_body, course_id))

def build_pads(course_id):
    pads_source_path = os.path.join(COURSE_PATH, course_id, 'pads')
    pad_filenames = [filename for filename in os.listdir(pads_source_path) if filename.endswith('.pypad.json')]

    pads_build_path = os.path.join(BUILD_PATH, 'pads', course_id)
    if not os.path.exists(pads_build_path):
        os.makedirs(pads_build_path)

    for pad_filename in pad_filenames:
        source_pad_file_path = os.path.join(pads_source_path, pad_filename)
        build_pad_file_path = os.path.join(pads_build_path, pad_filename)
        with open(source_pad_file_path, 'r') as f:
            pad_body = f.read()
        with open(build_pad_file_path, 'w') as f:
            f.write(pad_body)
        generate_hash_for_pad(build_pad_file_path)

def build_assets(course_id):
    assets_source_path = os.path.join(COURSE_PATH, course_id, 'assets')
    assets_build_path = os.path.join(BUILD_PATH, 'static', course_id)
    if os.path.exists(assets_build_path):
        shutil.rmtree(assets_build_path)
    shutil.copytree(assets_source_path, assets_build_path)

def main():
    init_target_path()
    course_ids = get_course_ids()
    for course_id in course_ids:
        build_table(course_id)
        build_docs(course_id)
        build_pads(course_id)
        build_assets(course_id)

if __name__ == '__main__':
    main()

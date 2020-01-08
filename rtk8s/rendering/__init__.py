import os
import shutil
import jinja2


def render_string(s, config):
    t = jinja2.Environment(loader=jinja2.BaseLoader).from_string(s)
    return t.render(**config)


def render_project(templates, target, config, markers=(".j2",), overwrite=False):
    for root, dirs, files in os.walk(templates):
        for file in files:

            filename, ext = os.path.splitext(file)

            src = os.path.join(root, file)
            dst_path = os.path.join(target, root.replace(templates, ""))

            if not os.path.exists(dst_path):
                os.makedirs(dst_path)

            if ext in markers:

                dst = os.path.join(dst_path, filename)

                with open(src, "r") as src_file:
                    if not os.path.exists(dst) or overwrite:
                        with open(dst, "w") as dst_file:
                            s = render_string(src_file.read(), config)
                            dst_file.write(s)
                    else:
                        print(f"Skipping {dst} - it already exists!")

            else:
                dst = os.path.join(dst_path, file)
                shutil.copy2(src, dst)


__all__ = [
    "render_project",
    "render_string"
]

"""Public HTML outputs, excluding internal build and export templates."""
def generated_pages(root):
    return sorted([*root.glob('*.html'),*(root/'en').glob('*.html'),*(root/'sq').glob('*.html'),*(root/'angebot').glob('*.html')])

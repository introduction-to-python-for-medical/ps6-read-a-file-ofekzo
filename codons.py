def create_codon_dict(file_path):
    dicofco={}
    for r in rows[0:]:
      
      cells=r.strip().split('\t')
      key = cells[0]
      value = cells[2]
      dicofco[key] = value
    return dicofco



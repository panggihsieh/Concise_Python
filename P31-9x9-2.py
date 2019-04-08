for outer in range(1,6):
    for inner in range(1,6):
        print('{:>1}x{:>1}={:>2}'.format(outer,inner,outer*inner),
              end='\t')
    print()

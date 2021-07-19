def get_pagination_range(current_page, max_index):
  if max_index < 5:
    start_index = 1
    end_index = max_index

  else:
    if current_page - 2 <= 0 or current_page + 2 >= max_index:
      if current_page - 2 <= 0:
        start_index = 1
        end_index = 5
      else:
        start_index = max_index - 4
        end_index = max_index
    else:
      start_index = current_page - 2
      end_index = current_page + 2

  return start_index-1, end_index
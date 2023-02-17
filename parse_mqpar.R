parse_mqpar <- function(file) {
  x <- XML::xmlParse(file)
  l <- XML::xmlToList(x)
  
  df <- data.frame(
    filePaths = unlist(l$filePaths),
    experiments = unlist(l$experiments),
    fractions = unlist(l$fractions),
    ptms = unlist(l$ptms),
    paramGroupIndices = unlist(l$paramGroupIndices)
  )
  
  if (is.null(rc <- unlist(l$referenceChannel)))
    df$referenceChannel <- "NULL" else
      df$referenceChannel <- rc
  
  list(
    fasta = l$fastaFiles$FastaFileInfo$fastaFilePath,
    experimental_design = df
  )
}

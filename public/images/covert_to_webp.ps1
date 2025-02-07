Get-ChildItem -Filter "*.png" | ForEach-Object {
    $inputFile = $_.FullName
    $outputFile = ($inputFile -replace "\.png$") + ".webp"
    cwebp "$inputFile" -o "$outputFile"
  }
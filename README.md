# TourML description extractor
TourML description extractor aims at extracting knowledge from natural language description associated with TourML stops within an input file.
The extraction is performed by [FRED](http://wit.istc.cnr.it/stlab-tools/fred/).

### Installation and usage

You can install and run the script usign [Anaconda](https://www.anaconda.com/) as follows.
1. Create an environment

```
conda env create -f environment.yml
```

2. Activate the environment

```
conda activate fred_dial    
```

3. Run the script

```
python TourML_description_extractor.py /path/to/tourML/file.xml /output/folder FRED_URL RDF_MIME_TYPE BASE_URI_FOR_FRED_RESOURCES
```

### License

This software is distributed under [Apache 2.0 License](LICENSE)

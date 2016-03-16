
/////////////////////==========================/////////////
///////////////////////// DUCKMASTER 2015 /////////////////
/////////////////////\/\/\/\/\/\\//\/\/\/\//\/\///////////

//////////// interfejs ////////////////////////////////
//////////////////////////////////////////////////////

// VAZNO !!!! ->-> Ne zajebavaj se s navodnicima ///////

//--------------- Izmedju navodnika paste naziv stripa, izdanja....
//--------------- To ce ti biti naziv foldera na Desktop-u i fajlova

var nazivStripa = "ALMANAH BROJ 3323"   ;

//--------------- Ovde mozes da menjas font broja stranice --------

var izaberiFont   = "Tahoma"            ;
var velicinaFonta =  20                 ;

//--------- Da promenis boju fonta, zameni RGB vrednosti ---------

var crvena = 115     ;
var zelena = 193     ;
var plava  = 236     ;

//////////// ispod ovoga ne diraj /////////////////////
//////////////////////////////////////////////////////

var outputAdresa = "D:/Documents and Settings/Owner/Desktop"     ;
var outputi      =  outputAdresa + "/" + nazivStripa             ;

var startDisplayDialogs  = app .displayDialogs   ;
app .displayDialogs      = DialogModes .NO       ;
var inputFolder          = Folder .selectDialog( "Izaberi Patke", "C:/test" ) ;

var outputFolder = new Folder( outputi )    ;
outputFolder .create( )                     ;


if ( inputFolder != null  &&  outputFolder != null )
{
	var fileList         = inputFolder .getFiles( "*.jpg" )   ;
	var jpegOptions      = new JPEGSaveOptions( )             ;
	jpegOptions .quality = 4                                  ;

	var textColor = new SolidColor           ;

	    textColor .rgb .red   = crvena       ;
	    textColor .rgb .green = zelena       ;
	    textColor .rgb .blue  = plava        ;


	for ( var i = 0;  i < fileList .length;  i ++ )
	{


		if ( fileList[i] instanceof File  &&  fileList[i] .hidden == false ) 
		{
			var docRef        = open( fileList[i] )         ;
			var newLayerRef   = docRef .artLayers .add( )   ;
			newLayerRef .kind = LayerKind .TEXT             ;

			if ( i > 0 )
			{
				var textItemRef = newLayerRef .textItem ;

				textItemRef .contents = i               ;
				textItemRef .size     = velicinaFonta   ;
				textItemRef .position = [ 0.2, 0.5 ]    ;
				textItemRef .font     = izaberiFont     ;
				textItemRef .color    = textColor       ;
			}

			docRef .saveAs(  new File(   outputFolder 
				                       + "/" 
				                       + nazivStripa 
				                       + "_0" 
				                       + i 
				                       + ".jpg" 
				                     )

                           , jpegOptions

                          )                                    ;

			docRef .close( SaveOptions .DONOTSAVECHANGES )     ;
		}

	}

}

app .displayDialogs = startDisplayDialogs    ;










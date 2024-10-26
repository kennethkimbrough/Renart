// src/data
export const renaissanceArtworks = [
  {
    id: 1,
    title: "Mona Lisa",
    artist: "Leonardo da Vinci",
    year: "1503-1519",
    url: "https://upload.wikimedia.org/wikipedia/commons/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg",
    period: "High Renaissance",
    location: "Louvre Museum, Paris",
    description: "The most famous painting in the world, known for the subject's enigmatic smile."
  },
  {
    id: 2,
    title: "The Birth of Venus",
    artist: "Sandro Botticelli",
    year: "1485-1486",
    url: "https://upload.wikimedia.org/wikipedia/commons/0/0b/Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg",
    period: "Early Renaissance",
    location: "Uffizi Gallery, Florence",
    description: "One of the most famous paintings of the Renaissance, depicting Venus emerging from the sea."
  },
];

// categorize them by period
export const periods = {
  EARLY_RENAISSANCE: "Early Renaissance",
  HIGH_RENAISSANCE: "High Renaissance",
  NORTHERN_RENAISSANCE: "Northern Renaissance",
  VENETIAN_RENAISSANCE: "Venetian Renaissance"
};
const moreArtworks = [
  {
    id: 3,
    title: "The Last Supper",
    artist: "Leonardo da Vinci",
    year: "1495-1498",
    url: "https://upload.wikimedia.org/wikipedia/commons/4/4b/%C3%9Altima_Cena_-_Da_Vinci_5.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Santa Maria delle Grazie, Milan",
    description: "One of the most famous religious paintings depicting Jesus's last supper with his apostles."
  },
  {
    id: 4,
    title: "The School of Athens",
    artist: "Raphael",
    year: "1509-1511",
    url: "https://upload.wikimedia.org/wikipedia/commons/4/49/%22The_School_of_Athens%22_by_Raffaello_Sanzio_da_Urbino.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Vatican Museums, Vatican City",
    description: "A fresco depicting the greatest mathematicians, philosophers and scientists of classical antiquity."
  },
  {
    id: 5,
    title: "The Creation of Adam",
    artist: "Michelangelo",
    year: "1508-1512",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5b/Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Sistine Chapel, Vatican City",
    description: "Part of the Sistine Chapel ceiling, depicting God giving life to Adam."
  },
  {
    id: 6,
    title: "The Arnolfini Portrait",
    artist: "Jan van Eyck",
    year: "1434",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/33/Van_Eyck_-_Arnolfini_Portrait.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, London",
    description: "A masterpiece of Northern Renaissance art, showing incredible detail and symbolism."
  },
  {
    id: 7,
    title: "Primavera",
    artist: "Sandro Botticelli",
    year: "1477-1482",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/3c/Botticelli-primavera.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "An allegorical painting representing the arrival of spring."
  },
  {
    id: 8,
    title: "Venus of Urbino",
    artist: "Titian",
    year: "1538",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/bb/Tiziano_-_Venere_di_Urbino_-_Google_Art_Project.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "A masterpiece of the Venetian Renaissance, depicting Venus as an idealized female figure."
  },
  {
    id: 9,
    title: "The Garden of Earthly Delights",
    artist: "Hieronymus Bosch",
    year: "1490-1510",
    url: "https://upload.wikimedia.org/wikipedia/commons/a/ae/El_jardín_de_las_Delicias%2C_de_El_Bosco.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "A complex triptych depicting paradise, earthly pleasures, and hell."
  },
  {
    id: 10,
    title: "Madonna of the Meadow",
    artist: "Raphael",
    year: "1506",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5c/Raphael_-_Madonna_in_the_Meadow_-_Google_Art_Project.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "A serene depiction of the Virgin Mary with Jesus and John the Baptist as children."
  },
  {
    id: 11,
    title: "The Ambassadors",
    artist: "Hans Holbein the Younger",
    year: "1533",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/88/Hans_Holbein_the_Younger_-_The_Ambassadors_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Famous for its anamorphic skull and rich symbolic elements."
  },
  {
    id: 12,
    title: "Assumption of the Virgin",
    artist: "Titian",
    year: "1515-1518",
    url: "https://upload.wikimedia.org/wikipedia/commons/c/c3/Tizian_041.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Basilica di Santa Maria Gloriosa dei Frari, Venice",
    description: "A masterpiece showing the Virgin Mary's ascension into heaven."
  },
  {
    id: 13,
    title: "Doni Tondo",
    artist: "Michelangelo",
    year: "1507",
    url: "https://upload.wikimedia.org/wikipedia/commons/4/4d/Michelangelo_Buonarroti_-_Tondo_Doni_-_Google_Art_Project.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "A unique circular painting depicting the Holy Family."
  },
  {
    id: 14,
    title: "The Annunciation",
    artist: "Fra Angelico",
    year: "1440-1445",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/1b/Fra_Angelico_-_The_Annunciation_-_WGA00555.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Convent of San Marco, Florence",
    description: "A fresco showing the angel Gabriel announcing to Mary that she would bear Jesus."
  },
  {
    id: 15,
    title: "Portrait of a Man in a Red Turban",
    artist: "Jan van Eyck",
    year: "1433",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/33/Portrait_of_a_Man_in_a_Red_Turban_%28Jan_van_Eyck%29.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Believed to be a self-portrait of the artist, showing remarkable detail."
  },
  {
    id: 16,
    title: "The Tempest",
    artist: "Giorgione",
    year: "1506-1508",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8c/Giorgione_019.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Gallerie dell'Accademia, Venice",
    description: "A mysterious painting whose meaning has been debated for centuries."
  },
  {
    id: 17,
    title: "Lady with an Ermine",
    artist: "Leonardo da Vinci",
    year: "1489-1490",
    url: "https://upload.wikimedia.org/wikipedia/commons/e/ed/Lady_with_an_Ermine_-_Leonardo_da_Vinci_-_Google_Art_Project.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Czartoryski Museum, Kraków",
    description: "A portrait of Cecilia Gallerani, mistress of Ludovico Sforza."
  },
  {
    id: 18,
    title: "The Battle of San Romano",
    artist: "Paolo Uccello",
    year: "1438-1440",
    url: "https://upload.wikimedia.org/wikipedia/commons/e/e4/Paolo_Uccello_016.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "A series of three paintings depicting a battle between Florentine and Sienese forces."
  },
  {
    id: 19,
    title: "The Ghent Altarpiece",
    artist: "Jan van Eyck",
    year: "1432",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/55/Retable_de_l%27Agneau_mystique.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Saint Bavo's Cathedral, Ghent",
    description: "One of the most important and complex masterpieces of Northern Renaissance art."
  },
  {
    id: 20,
    title: "Sacred and Profane Love",
    artist: "Titian",
    year: "1514",
    url: "https://upload.wikimedia.org/wikipedia/commons/e/ed/Sacred_and_Profane_Love_by_Titian.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Galleria Borghese, Rome",
    description: "An allegorical painting contrasting earthly and divine love."
  },
  {
    id: 21,
    title: "Lamentation of Christ",
    artist: "Andrea Mantegna",
    year: "1480",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/89/Andrea_Mantegna_-_The_Lamentation_over_the_Dead_Christ_-_WGA13981.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Pinacoteca di Brera, Milan",
    description: "Famous for its dramatic foreshortening and emotional intensity."
  },
  {
    id: 22,
    title: "Portrait of Baldassare Castiglione",
    artist: "Raphael",
    year: "1515",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/85/Baldassare_Castiglione%2C_by_Raffaello_Sanzio%2C_from_C2RMF_retouched.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Louvre Museum, Paris",
    description: "A portrait of the influential Renaissance author and diplomat."
  },
  {
    id: 23,
    title: "The Battle of Alexander at Issus",
    artist: "Albrecht Altdorfer",
    year: "1529",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f3/Albrecht_Altdorfer_-_The_Battle_of_Alexander_at_Issus_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Alte Pinakothek, Munich",
    description: "A dramatic battle scene with incredible detail and cosmic background."
  },
  {
    id: 24,
    title: "Feast in the House of Levi",
    artist: "Paolo Veronese",
    year: "1573",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/3f/Paolo_Veronese_-_Feast_at_the_House_of_Levi_-_WGA24886.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Gallerie dell'Accademia, Venice",
    description: "A monumental painting originally intended as a Last Supper."
  },
  {
    id: 25,
    title: "St. George and the Dragon",
    artist: "Paolo Uccello",
    year: "1470",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8d/Paolo_Uccello_047.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "National Gallery, London",
    description: "Shows the artist's fascination with perspective and chivalric subjects."
  },
  {
    id: 26,
    title: "Susanna and the Elders",
    artist: "Tintoretto",
    year: "1555",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5e/Susanna_and_the_Elders_%28Tintoretto%29.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "A dramatic interpretation of the biblical story."
  },
  {
    id: 27,
    title: "The Crucifixion",
    artist: "Fra Angelico",
    year: "1441-1442",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/1b/Fra_Angelico_027.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Convent of San Marco, Florence",
    description: "A fresco showing remarkable spiritual intensity and compositional harmony."
  },
  {
    id: 28,
    title: "Madonna del Granduca",
    artist: "Raphael",
    year: "1505",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Raffaello_Madonna_del_Granduca.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Palazzo Pitti, Florence",
    description: "A tender portrayal of the Virgin and Child."
  },
  {
    id: 29,
    title: "The Allegory of Good and Bad Government",
    artist: "Ambrogio Lorenzetti",
    year: "1338-1339",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9d/Ambrogio_Lorenzetti_-_Effects_of_Good_Government_in_the_city_-_Google_Art_Project.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Palazzo Pubblico, Siena",
    description: "A series of frescoes showing the effects of good and bad governance."
  },
  {
    id: 30,
    title: "Self-Portrait with Fur-Trimmed Robe",
    artist: "Albrecht Dürer",
    year: "1500",
    url: "https://upload.wikimedia.org/wikipedia/commons/4/4e/Albrecht_D%C3%BCrer_-_Self-Portrait_at_28_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Alte Pinakothek, Munich",
    description: "A striking self-portrait showing the artist in Christ-like pose."
  },
  {
    id: 31,
    title: "The Descent from the Cross",
    artist: "Rogier van der Weyden",
    year: "1435",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/1a/Descent_from_the_cross_-_Rogier_van_der_Weyden.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "A masterpiece of emotional expression in Northern Renaissance art."
  },
  {
    id: 32,
    title: "Portrait of a Young Man",
    artist: "Bronzino",
    year: "1530",
    url: "https://upload.wikimedia.org/wikipedia/commons/7/7d/Angelo_Bronzino_-_Portrait_of_a_Young_Man_-_Google_Art_Project.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Metropolitan Museum of Art, New York",
    description: "A masterpiece of Mannerist portraiture."
  },
  {
    id: 33,
    title: "The Money Changer and His Wife",
    artist: "Quentin Matsys",
    year: "1514",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f1/Quentin_Matsys_-_The_Money_Changer_and_His_Wife_-_WGA14281.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Louvre Museum, Paris",
    description: "A detailed portrayal of a money changer and his wife, rich in symbolism."
  },
  {
    id: 34,
    title: "The Annunciation",
    artist: "Leonardo da Vinci",
    year: "1472-1475",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/39/Leonardo_da_Vinci_-_Annunciazione_-_Google_Art_Project.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "One of Leonardo's earliest surviving works, showing his mastery of perspective."
  },
  {
    id: 35,
    title: "The Triumph of Galatea",
    artist: "Raphael",
    year: "1511",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/The_Triumph_of_Galatea_by_Raphael.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Villa Farnesina, Rome",
    description: "A fresco depicting the mythological figure Galatea."
  },
  {
    id: 36,
    title: "Portrait of Doge Leonardo Loredan",
    artist: "Giovanni Bellini",
    year: "1501",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/be/Giovanni_Bellini%2C_portrait_of_Doge_Leonardo_Loredan.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Official portrait of the Doge of Venice showing incredible detail in fabric and jewelry."
  },
  {
    id: 37,
    title: "The Resurrection of Christ",
    artist: "Piero della Francesca",
    year: "1463",
    url: "https://upload.wikimedia.org/wikipedia/commons/6/65/Piero_della_Francesca_-_Resurrection_-_WGA17609.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museo Civico, Sansepolcro",
    description: "A masterpiece showing Christ's triumphant resurrection."
  },
  {
    id: 38,
    title: "Portrait of a Lady with a Squirrel and a Starling",
    artist: "Hans Holbein the Younger",
    year: "1526-1528",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f2/Hans_Holbein_the_Younger_-_A_Lady_with_a_Squirrel_and_a_Starling.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, London",
    description: "A detailed portrait showing Holbein's mastery of observation."
  },
  {
    id: 39,
    title: "Feast of the Gods",
    artist: "Giovanni Bellini",
    year: "1514",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8a/The_Feast_of_the_Gods_-_Giovanni_Bellini_-_National_Gallery_of_Art.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "National Gallery of Art, Washington D.C.",
    description: "A mythological scene completed late in Bellini's life."
  },
  {
    id: 40,
    title: "The Torment of Saint Anthony",
    artist: "Michelangelo",
    year: "1487-1488",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/95/Michelangelo_Buonarroti_-_The_Torment_of_Saint_Anthony_-_Google_Art_Project.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Kimbell Art Museum, Fort Worth",
    description: "One of Michelangelo's earliest known paintings."
  },
  {
    id: 41,
    title: "The Dream of Saint Helena",
    artist: "Paolo Veronese",
    year: "1570",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5c/Paolo_Veronese_-_The_Dream_of_Saint_Helena_-_WGA24882.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Depicts Saint Helena's dream of finding the True Cross."
  },
  {
    id: 42,
    title: "The Battle of the Angels",
    artist: "Albrecht Dürer",
    year: "1498",
    url: "https://upload.wikimedia.org/wikipedia/commons/7/7f/Albrecht_D%C3%BCrer_-_Saint_Michael_Fighting_the_Dragon_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Various Collections",
    description: "A dramatic woodcut showing the battle between good and evil."
  },
  {
    id: 43,
    title: "Madonna of the Harpies",
    artist: "Andrea del Sarto",
    year: "1517",
    url: "https://upload.wikimedia.org/wikipedia/commons/a/a5/Andrea_del_Sarto_-_Madonna_of_the_Harpies_-_Google_Art_Project.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "A masterpiece showing the Virgin Mary standing on a pedestal decorated with harpies."
  },
  {
    id: 44,
    title: "The Hunters in the Snow",
    artist: "Pieter Bruegel the Elder",
    year: "1565",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d8/Pieter_Bruegel_the_Elder_-_Hunters_in_the_Snow_%28Winter%29_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Part of a series depicting different seasons, showing a winter landscape."
  },
  {
    id: 45,
    title: "The Finding of the True Cross",
    artist: "Piero della Francesca",
    year: "1460",
    url: "https://upload.wikimedia.org/wikipedia/commons/7/7c/Discovery_and_Proof_of_the_True_Cross%2C_Piero_della_Francesca.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Basilica of San Francesco, Arezzo",
    description: "Part of a fresco cycle depicting the Legend of the True Cross."
  },
// Continuing the moreArtworks array...

  {
    id: 46,
    title: "Allegory of Spring and Summer",
    artist: "Giuseppe Arcimboldo",
    year: "1563",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/3f/Giuseppe_Arcimboldo_-_Spring_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Louvre Museum, Paris",
    description: "Famous portrait made entirely of flowers and plants."
  },
  {
    id: 47,
    title: "The Crucifixion",
    artist: "Matthias Grünewald",
    year: "1515",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d3/Mathis_Gothart_Gr%C3%BCnewald_-_The_Crucifixion_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Unterlinden Museum, Colmar",
    description: "Part of the Isenheim Altarpiece, known for its emotional intensity."
  },
  {
    id: 48,
    title: "Portrait of Federico da Montefeltro",
    artist: "Piero della Francesca",
    year: "1465-1472",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d9/Piero_della_Francesca_044.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Famous profile portrait of the Duke of Urbino."
  },
  {
    id: 49,
    title: "Assumption of the Virgin",
    artist: "Correggio",
    year: "1526-1530",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/87/Correggio_-_Assumption_of_the_Virgin_-_Cathedral_of_Parma.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Cathedral of Parma",
    description: "Revolutionary dome fresco with dramatic foreshortening."
  },
  {
    id: 50,
    title: "The Peasant Wedding",
    artist: "Pieter Bruegel the Elder",
    year: "1567",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/b7/Pieter_Bruegel_the_Elder_-_Peasant_Wedding_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Detailed depiction of peasant life and celebrations."
  },
  {
    id: 51,
    title: "Flora",
    artist: "Titian",
    year: "1515",
    url: "https://upload.wikimedia.org/wikipedia/commons/4/47/Tizian_085.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Portrait of a young woman personifying the goddess of flowers."
  },
  {
    id: 52,
    title: "The Adoration of the Magi",
    artist: "Gentile da Fabriano",
    year: "1423",
    url: "https://upload.wikimedia.org/wikipedia/commons/7/7c/Gentile_da_Fabriano_001.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Ornate altarpiece with extensive use of gold leaf."
  },
  {
    id: 53,
    title: "Christ Carrying the Cross",
    artist: "Hieronymus Bosch",
    year: "1515-1516",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d3/Christ_Carrying_the_Cross_-_Bosch.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museum of Fine Arts, Ghent",
    description: "Grotesque faces surrounding Christ in his suffering."
  },
  {
    id: 54,
    title: "The Feast of the Rosary",
    artist: "Albrecht Dürer",
    year: "1506",
    url: "https://upload.wikimedia.org/wikipedia/commons/c/c6/Albrecht_D%C3%BCrer_-_Feast_of_Rose_Garlands_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, Prague",
    description: "Commissioned for the German community in Venice."
  },
  {
    id: 55,
    title: "Portrait of a Young Woman",
    artist: "Petrus Christus",
    year: "1470",
    url: "https://upload.wikimedia.org/wikipedia/commons/6/66/Petrus_Christus_-_Portrait_of_a_Young_Woman_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Gemäldegalerie, Berlin",
    description: "Innovative three-quarter view portrait."
  },
  {
    id: 56,
    title: "The Presentation of Christ in the Temple",
    artist: "Fra Angelico",
    year: "1442",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8c/Fra_Angelico_-_Presentation_of_Jesus_in_the_Temple_-_WGA00513.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "San Marco Museum, Florence",
    description: "Part of the San Marco altarpiece."
  },
  {
    id: 57,
    title: "Portrait of Giovanni Arnolfini",
    artist: "Jan van Eyck",
    year: "1435",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9d/Giovanni_Arnolfini.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Gemäldegalerie, Berlin",
    description: "Individual portrait of the merchant from the famous Arnolfini couple."
  },
  {
    id: 58,
    title: "Madonna with the Long Neck",
    artist: "Parmigianino",
    year: "1534-1540",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/bc/Parmigianino_-_Madonna_dal_collo_lungo_-_Google_Art_Project.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Mannerist masterpiece with elongated proportions."
  },
  {
    id: 59,
    title: "The Tower of Babel",
    artist: "Pieter Bruegel the Elder",
    year: "1563",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/fc/Pieter_Bruegel_the_Elder_-_The_Tower_of_Babel_%28Vienna%29_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Detailed depiction of the biblical tower's construction."
  },
  {
    id: 60,
    title: "Perseus with the Head of Medusa",
    artist: "Benvenuto Cellini",
    year: "1545-1554",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/96/Persee_Cellini_Loggia_dei_Lanzi_2005_09_13.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Loggia dei Lanzi, Florence",
    description: "Bronze sculpture showing Perseus triumphant over Medusa."
  },
  {
    id: 61,
    title: "The Garden of Earthly Delights",
    artist: "Hieronymus Bosch",
    year: "1490-1510",
    url: "https://upload.wikimedia.org/wikipedia/commons/a/ae/El_jard%C3%ADn_de_las_Delicias%2C_de_El_Bosco.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "Triptych depicting paradise, earthly pleasures, and hell."
  },
  {
    id: 62,
    title: "The Tempest",
    artist: "Giorgione",
    year: "1506-1508",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8c/Giorgione_019.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Gallerie dell'Accademia, Venice",
    description: "Mysterious painting with enigmatic figures in a stormy landscape."
  },
  {
    id: 63,
    title: "The Death of the Virgin",
    artist: "Hugo van der Goes",
    year: "1472-1480",
    url: "https://upload.wikimedia.org/wikipedia/commons/2/23/Hugo_van_der_Goes_-_The_Death_of_the_Virgin_-_WGA09502.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Groeningemuseum, Bruges",
    description: "Emotional depiction of the Virgin Mary's death."
  },
  {
    id: 64,
    title: "Judith with the Head of Holofernes",
    artist: "Lucas Cranach the Elder",
    year: "1530",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/3c/Lucas_Cranach_d.%C3%84._-_Judith_mit_dem_Haupt_des_Holofernes.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Biblical heroine depicted in contemporary German dress."
  },
  {
    id: 65,
    title: "The Doge on Shrove Tuesday",
    artist: "Giovanni Bellini",
    year: "1500",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5b/Giovanni_Bellini_-_Procession_in_St._Mark%27s_Square_-_Google_Art_Project.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Gallerie dell'Accademia, Venice",
    description: "Detailed view of Venetian ceremonial life."
  },
  {
    id: 66,
    title: "The Seven Deadly Sins",
    artist: "Hieronymus Bosch",
    year: "1485",
    url: "https://upload.wikimedia.org/wikipedia/commons/2/2c/Hieronymus_Bosch-_The_Seven_Deadly_Sins_and_the_Four_Last_Things.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "Table top painting depicting the seven deadly sins."
  },
  {
    id: 67,
    title: "The Mystic Marriage of Saint Catherine",
    artist: "Lorenzo Lotto",
    year: "1524",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8f/Lorenzo_Lotto_-_Mystic_Marriage_of_St_Catherine_-_WGA13710.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Gallerie dell'Accademia, Venice",
    description: "Dynamic composition showing the mystical union of Saint Catherine with Christ."
  },
  {
    id: 68,
    title: "The Conversion of Saint Paul",
    artist: "Caravaggio",
    year: "1601",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f6/Conversion_on_the_Way_to_Damascus-Caravaggio_%28c.1600-1%29.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Santa Maria del Popolo, Rome",
    description: "Dramatic depiction of Saul's conversion on the road to Damascus."
  },
  {
    id: 69,
    title: "The Allegory of Good Government",
    artist: "Ambrogio Lorenzetti",
    year: "1338-1339",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f8/Ambrogio_Lorenzetti_-_Allegory_of_Good_Government_-_Google_Art_Project.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Palazzo Pubblico, Siena",
    description: "Fresco cycle depicting the effects of good governance on city life."
  },
  {
    id: 70,
    title: "The Baptism of Christ",
    artist: "Piero della Francesca",
    year: "1448-1450",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/3d/Piero_della_Francesca_-_Baptism_of_Christ_-_WGA17595.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "National Gallery, London",
    description: "Masterpiece showing geometric composition and light effects."
  },
  {
    id: 71,
    title: "The Fall of Icarus",
    artist: "Pieter Bruegel the Elder",
    year: "1558",
    url: "https://upload.wikimedia.org/wikipedia/commons/c/c2/Pieter_Bruegel_the_Elder_-_Landscape_with_the_Fall_of_Icarus_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Royal Museums of Fine Arts, Brussels",
    description: "Landscape where Icarus's fall is a minor detail in daily life."
  },
  {
    id: 72,
    title: "Portrait of a Man in a Red Turban",
    artist: "Jan van Eyck",
    year: "1433",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d7/Portrait_of_a_Man_in_a_Red_Turban_%28Jan_van_Eyck%29.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Possibly a self-portrait of the artist."
  },
  {
    id: 73,
    title: "The Battle of San Romano",
    artist: "Paolo Uccello",
    year: "1438-1440",
    url: "https://upload.wikimedia.org/wikipedia/commons/e/e4/Paolo_Uccello_049.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Famous battle scene showing mastery of perspective."
  },
  {
    id: 74,
    title: "The Ambassadors",
    artist: "Hans Holbein the Younger",
    year: "1533",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/88/Hans_Holbein_the_Younger_-_The_Ambassadors_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Double portrait with famous anamorphic skull."
  },
// Continuing the moreArtworks array...

  {
    id: 75,
    title: "The Assumption of the Virgin",
    artist: "Titian",
    year: "1516-1518",
    url: "https://upload.wikimedia.org/wikipedia/commons/a/a6/Tizian_041.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Basilica di Santa Maria Gloriosa dei Frari, Venice",
    description: "Monumental altarpiece showing dynamic upward movement."
  },
  {
    id: 76,
    title: "The Last Judgment",
    artist: "Fra Angelico",
    year: "1431",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5a/Fra_Angelico_-_The_Last_Judgement_%28Winged_Altar%29_-_Google_Art_Project.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museum of San Marco, Florence",
    description: "Detailed depiction of souls ascending to heaven and descending to hell."
  },
  {
    id: 77,
    title: "The Ghent Altarpiece (Adoration of the Mystic Lamb)",
    artist: "Jan van Eyck",
    year: "1432",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5c/Retable_de_l%27Agneau_mystique.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Saint Bavo Cathedral, Ghent",
    description: "Masterpiece of Early Netherlandish painting."
  },
  {
    id: 78,
    title: "Madonna of the Meadow",
    artist: "Raphael",
    year: "1506",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5c/Raphael_-_Madonna_in_the_Meadow_-_Google_Art_Project.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Harmonious composition showing the Virgin with Christ and John the Baptist."
  },
  {
    id: 79,
    title: "The Descent from the Cross",
    artist: "Rogier van der Weyden",
    year: "1435",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/1a/Descent_from_the_cross_-_Rogier_van_der_Weyden.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "Emotional depiction of Christ's body being removed from the cross."
  },
  {
    id: 80,
    title: "Portrait of Baldassare Castiglione",
    artist: "Raphael",
    year: "1515",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/85/Raphael_-_Portrait_of_Baldassare_Castiglione_-_Google_Art_Project.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Louvre Museum, Paris",
    description: "Portrait of the famous Renaissance author and diplomat."
  },
  {
    id: 81,
    title: "The Battle of Alexander at Issus",
    artist: "Albrecht Altdorfer",
    year: "1529",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f3/Albrecht_Altdorfer_-_The_Battle_of_Alexander_at_Issus_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Alte Pinakothek, Munich",
    description: "Dramatic battle scene with cosmic landscape."
  },
  {
    id: 82,
    title: "Maestà",
    artist: "Duccio",
    year: "1308-1311",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8d/Duccio_di_Buoninsegna_-_Maest%C3%A0_%28front%29_-_Google_Art_Project.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museo dell'Opera del Duomo, Siena",
    description: "Monumental altarpiece that influenced early Renaissance art."
  },
  {
    id: 83,
    title: "The Annunciation",
    artist: "Jan van Eyck",
    year: "1434-1436",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/89/Van_Eyck_-_The_Annunciation.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery of Art, Washington D.C.",
    description: "Detailed church interior with symbolic elements."
  },
  {
    id: 84,
    title: "The Healing of the Cripple",
    artist: "Masaccio",
    year: "1426-1427",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/b2/Masaccio_-_St_Peter_Healing_the_Sick_with_his_Shadow_-_WGA14247.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Brancacci Chapel, Florence",
    description: "Fresco showing revolutionary use of perspective and naturalism."
  },
  {
    id: 85,
    title: "Self-Portrait",
    artist: "Albrecht Dürer",
    year: "1500",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/dc/Albrecht_D%C3%BCrer_-_Self-Portrait_%281500%29_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Alte Pinakothek, Munich",
    description: "Famous frontal self-portrait in the image of Christ."
  },
  {
    id: 86,
    title: "The Crucifixion of Saint Peter",
    artist: "Caravaggio",
    year: "1601",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f5/Caravaggio_-_Crucifixion_of_Saint_Peter.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Santa Maria del Popolo, Rome",
    description: "Dramatic depiction of Saint Peter's martyrdom."
  },
  {
    id: 87,
    title: "The Allegory of Spring",
    artist: "Sandro Botticelli",
    year: "1482",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/3c/Botticelli-primavera.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Complex allegorical painting with mythological figures."
  }
// Continuing the moreArtworks array...

  {
    id: 88,
    title: "The Legend of the True Cross",
    artist: "Piero della Francesca",
    year: "1452-1466",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8e/Piero_della_Francesca_-_Discovery_and_Proof_of_the_True_Cross_-_WGA17585.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Basilica of San Francesco, Arezzo",
    description: "Fresco cycle depicting the history of the True Cross."
  },
  {
    id: 89,
    title: "The Money Changer and His Wife",
    artist: "Quentin Matsys",
    year: "1514",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f1/Quentin_Matsys_-_The_Money_Changer_and_His_Wife_-_WGA14281.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Louvre Museum, Paris",
    description: "Detailed portrayal of a merchant couple counting money."
  },
  {
    id: 90,
    title: "The Resurrection",
    artist: "Piero della Francesca",
    year: "1463-1465",
    url: "https://upload.wikimedia.org/wikipedia/commons/6/65/Piero_della_Francesca_-_Resurrection_-_WGA17609.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museo Civico, Sansepolcro",
    description: "Iconic image of Christ rising from the tomb."
  },
  {
    id: 91,
    title: "The Hunters in the Snow",
    artist: "Pieter Bruegel the Elder",
    year: "1565",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d8/Pieter_Bruegel_the_Elder_-_Hunters_in_the_Snow_%28Winter%29_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Winter landscape showing returning hunters and village life."
  },
  {
    id: 92,
    title: "Venus of Urbino",
    artist: "Titian",
    year: "1538",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/bb/Tiziano_-_Venere_di_Urbino_-_Google_Art_Project.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Sensual portrayal of Venus in a domestic setting."
  },
  {
    id: 93,
    title: "The Last Supper",
    artist: "Dirk Bouts",
    year: "1464-1468",
    url: "https://upload.wikimedia.org/wikipedia/commons/2/29/Dirk_Bouts_-_The_Last_Supper_-_WGA03028.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "St. Peter's Church, Leuven",
    description: "Detailed depiction of the Last Supper with contemporary details."
  },
  {
    id: 94,
    title: "The Finding of the True Cross",
    artist: "Agnolo Gaddi",
    year: "1380",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Agnolo_Gaddi_-_Legend_of_the_True_Cross_-_WGA8366.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Basilica of Santa Croce, Florence",
    description: "Fresco cycle depicting the legend of the True Cross."
  },
  {
    id: 95,
    title: "The Descent from the Cross",
    artist: "Fra Angelico",
    year: "1432-1434",
    url: "https://upload.wikimedia.org/wikipedia/commons/6/6f/Fra_Angelico_-_Descent_from_the_Cross_-_WGA00628.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museum of San Marco, Florence",
    description: "Emotional scene of Christ's body being removed from the cross."
  },
  {
    id: 96,
    title: "The Battle of San Romano",
    artist: "Paolo Uccello",
    year: "1438-1440",
    url: "https://upload.wikimedia.org/wikipedia/commons/e/e4/Paolo_Uccello_049.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "National Gallery, London",
    description: "Dynamic battle scene showing mastery of perspective."
  },
  {
    id: 97,
    title: "The Judgment of Paris",
    artist: "Lucas Cranach the Elder",
    year: "1530",
    url: "https://upload.wikimedia.org/wikipedia/commons/2/2c/Lucas_Cranach_d._%C3%84._-_Das_Urteil_des_Paris.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Metropolitan Museum of Art, New York",
    description: "Mythological scene of Paris choosing between three goddesses."
  },
  {
    id: 98,
    title: "The Annunciation",
    artist: "Fra Filippo Lippi",
    year: "1443",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/bb/Fra_Filippo_Lippi_-_Annunciation_-_WGA13231.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "National Gallery, London",
    description: "Innovative composition of the angel Gabriel's announcement to Mary."
  },
  {
    id: 99,
    title: "The Garden of Paradise",
    artist: "Upper Rhenish Master",
    year: "1410",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9b/Meister_des_Frankfurter_Paradiesg%C3%A4rtleins_001.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Städel Museum, Frankfurt",
    description: "Detailed depiction of the Virgin and saints in an enclosed garden."
  },
  {
    id: 100,
    title: "The Triumph of Death",
    artist: "Pieter Bruegel the Elder",
    year: "1562",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/10/Pieter_Bruegel_the_Elder_-_The_Triumph_of_Death_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "Apocalyptic landscape showing death's triumph over all walks of life."
  }
// Continuing the moreArtworks array...

  {
    id: 101,
    title: "Portrait of a Young Woman",
    artist: "Petrus Christus",
    year: "1470",
    url: "https://upload.wikimedia.org/wikipedia/commons/6/66/Petrus_Christus_-_Portrait_of_a_Young_Woman_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Gemäldegalerie, Berlin",
    description: "Elegant portrait showing detailed costume and jewelry."
  },
  {
    id: 102,
    title: "The Presentation in the Temple",
    artist: "Andrea Mantegna",
    year: "1460",
    url: "https://upload.wikimedia.org/wikipedia/commons/4/4e/Andrea_Mantegna_-_Presentation_at_the_Temple_-_WGA13945.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Gemäldegalerie, Berlin",
    description: "Biblical scene with remarkable perspective and architectural detail."
  },
  {
    id: 103,
    title: "Portrait of Giovanni Arnolfini and his Wife",
    artist: "Jan van Eyck",
    year: "1434",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/33/Van_Eyck_-_Arnolfini_Portrait.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Famous double portrait with complex symbolism and details."
  },
  {
    id: 104,
    title: "The Holy Trinity",
    artist: "Masaccio",
    year: "1428",
    url: "https://upload.wikimedia.org/wikipedia/commons/0/0f/Masaccio%2C_trinit%C3%A0.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Santa Maria Novella, Florence",
    description: "Revolutionary fresco demonstrating mathematical perspective."
  },
  {
    id: 105,
    title: "Madonna with the Long Neck",
    artist: "Parmigianino",
    year: "1534-1540",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/bc/Parmigianino_-_Madonna_dal_collo_lungo_-_Google_Art_Project.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Mannerist masterpiece with elongated figures."
  },
  {
    id: 106,
    title: "The Peasant Wedding",
    artist: "Pieter Bruegel the Elder",
    year: "1567",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9b/Pieter_Bruegel_the_Elder_-_Peasant_Wedding_-_Google_Art_Project_2.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Lively depiction of a rural wedding celebration."
  },
  {
    id: 107,
    title: "The Crucifixion",
    artist: "Matthias Grünewald",
    year: "1515",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/de/Mathis_Gothart_Gr%C3%BCnewald_-_The_Crucifixion_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Unterlinden Museum, Colmar",
    description: "Emotionally intense depiction of Christ's suffering."
  },
  {
    id: 108,
    title: "The Dream of Saint Helena",
    artist: "Paolo Veronese",
    year: "1570",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5e/Paolo_Veronese_-_The_Dream_of_Saint_Helena_-_WGA24314.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Elegant portrayal of Saint Helena's vision of the True Cross."
  },
  {
    id: 109,
    title: "The Procession to Calvary",
    artist: "Pieter Bruegel the Elder",
    year: "1564",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/1a/Pieter_Bruegel_the_Elder_-_The_Procession_to_Calvary_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Biblical scene set in contemporary Flemish landscape."
  },
  {
    id: 110,
    title: "The Feast of the Gods",
    artist: "Giovanni Bellini",
    year: "1514",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8a/Giovanni_Bellini_and_Titian_-_The_Feast_of_the_Gods_-_Google_Art_Project.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "National Gallery of Art, Washington D.C.",
    description: "Mythological scene completed by Titian after Bellini's death."
  },
  {
    id: 111,
    title: "The Last Judgment",
    artist: "Hans Memling",
    year: "1467-1471",
    url: "https://upload.wikimedia.org/wikipedia/commons/7/7d/Hans_Memling_-_The_Last_Judgment_triptych_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Museum, Gdańsk",
    description: "Triptych showing the final judgment of souls."
  },
  {
    id: 112,
    title: "The Feast in the House of Levi",
    artist: "Paolo Veronese",
    year: "1573",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/3f/Paolo_Veronese_-_Feast_at_the_House_of_Levi_-_WGA24886.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Gallerie dell'Accademia, Venice",
    description: "Monumental feast scene originally intended as Last Supper."
  },
  {
    id: 113,
    title: "The Tower of Babel",
    artist: "Pieter Bruegel the Elder",
    year: "1563",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/fc/Pieter_Bruegel_the_Elder_-_The_Tower_of_Babel_%28Vienna%29_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Detailed architectural fantasy of biblical tower."
  },
  {
    id: 114,
    title: "Portrait of a Lady with a Squirrel and a Starling",
    artist: "Hans Holbein the Younger",
    year: "1526-1528",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f7/Hans_Holbein_the_Younger_-_Portrait_of_a_Lady_with_a_Squirrel_and_a_Starling_%28Anne_Lovell%3F%29_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Detailed portrait with symbolic animals."
  },
  {
    id: 115,
    title: "The Madonna of the Roses",
    artist: "Sandro Botticelli",
    year: "1485",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/86/Madonna_of_the_Rose_Garden.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Delicate Madonna and Child surrounded by roses and angels."
  },
  {
    id: 116,
    title: "The Garden of Earthly Delights",
    artist: "Hieronymus Bosch",
    year: "1490-1510",
    url: "https://upload.wikimedia.org/wikipedia/commons/a/ae/El_jard%C3%ADn_de_las_Delicias%2C_de_El_Bosco.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "Complex triptych depicting paradise, earthly pleasures, and hell."
  },
  {
    id: 117,
    title: "Sacred and Profane Love",
    artist: "Titian",
    year: "1514",
    url: "https://upload.wikimedia.org/wikipedia/commons/e/ed/Sacred_and_Profane_Love_by_Titian.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Galleria Borghese, Rome",
    description: "Allegorical painting contrasting earthly and divine love."
  },
  {
    id: 118,
    title: "The Ambassadors",
    artist: "Hans Holbein the Younger",
    year: "1533",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/88/Hans_Holbein_the_Younger_-_The_Ambassadors_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Double portrait with symbolic objects and anamorphic skull."
  },
  {
    id: 119,
    title: "The Doge Leonardo Loredan",
    artist: "Giovanni Bellini",
    year: "1501",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8a/Giovanni_Bellini%2C_portrait_of_Doge_Leonardo_Loredan.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Official portrait of Venetian doge in ceremonial dress."
  },
  {
    id: 120,
    title: "The Fall of the Rebel Angels",
    artist: "Pieter Bruegel the Elder",
    year: "1562",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9d/Pieter_Bruegel_the_Elder_-_The_Fall_of_the_Rebel_Angels_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Royal Museums of Fine Arts, Brussels",
    description: "Chaotic scene of angels battling demons."
  },
  {
    id: 121,
    title: "The Death of the Virgin",
    artist: "Hugo van der Goes",
    year: "1472-1480",
    url: "https://upload.wikimedia.org/wikipedia/commons/2/23/Hugo_van_der_Goes_-_Death_of_the_Virgin_-_WGA09440.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Groeningemuseum, Bruges",
    description: "Emotional depiction of the Virgin Mary's death."
  },
  {
    id: 122,
    title: "The Battle of Anghiari",
    artist: "Leonardo da Vinci",
    year: "1505",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d3/Battle_of_Anghiari.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Lost work, known through copies",
    description: "Famous lost battle scene known through copies and sketches."
  },
  {
    id: 123,
    title: "The Carrying of the Cross",
    artist: "Hieronymus Bosch",
    year: "1515-1516",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d3/Hieronymus_Bosch_-_Christ_Carrying_the_Cross_-_WGA2513.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museum of Fine Arts, Ghent",
    description: "Grotesque faces surrounding Christ carrying the cross."
  },
  {
    id: 124,
    title: "The Legend of Saint Ursula",
    artist: "Vittore Carpaccio",
    year: "1490-1495",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/38/Vittore_Carpaccio_-_Dream_of_St_Ursula_-_WGA04336.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Gallerie dell'Accademia, Venice",
    description: "Cycle of paintings depicting Saint Ursula's life."
  },
  {
    id: 125,
    title: "The Seven Sorrows of the Virgin",
    artist: "Albrecht Dürer",
    year: "1496-1497",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9d/Albrecht_D%C3%BCrer_-_The_Seven_Sorrows_of_the_Virgin_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Alte Pinakothek, Munich",
    description: "Series depicting the Virgin Mary's seven sorrows."
  },
  {
    id: 126,
    title: "The Tempest",
    artist: "Giorgione",
    year: "1508",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8f/La_Tempesta_-_Giorgione_-_Gallerie_dell%27Accademia_-_Venice.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Gallerie dell'Accademia, Venice",
    description: "Mysterious landscape with nursing mother and standing soldier."
  },
  {
    id: 127,
    title: "The Marriage at Cana",
    artist: "Gerard David",
    year: "1503",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Gerard_David_-_The_Marriage_at_Cana_-_WGA6036.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Louvre Museum, Paris",
    description: "Biblical scene of Christ's first miracle."
  },
  {
    id: 128,
    title: "The Resurrection of Christ",
    artist: "Matthias Grünewald",
    year: "1515",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8d/Matthias_Gr%C3%BCnewald_-_The_Resurrection_-_WGA10765.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Unterlinden Museum, Colmar",
    description: "Dramatic depiction of Christ rising from the tomb."
  },
  {
    id: 129,
    title: "Portrait of a Young Man",
    artist: "Antonello da Messina",
    year: "1474",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8c/Antonello_da_Messina_-_Portrait_of_a_Man_-_National_Gallery_London.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "National Gallery, London",
    description: "Influential portrait showing Northern and Italian Renaissance fusion."
  },
  {
    id: 130,
    title: "The Harvesters",
    artist: "Pieter Bruegel the Elder",
    year: "1565",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d5/Pieter_Bruegel_the_Elder-_The_Harvesters_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Metropolitan Museum of Art, New York",
    description: "Panoramic view of peasants harvesting wheat."
  },
  {
    id: 131,
    title: "The Annunciation",
    artist: "Carlo Crivelli",
    year: "1486",
    url: "https://upload.wikimedia.org/wikipedia/commons/7/79/Carlo_Crivelli_007.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "National Gallery, London",
    description: "Elaborate architectural setting for the Annunciation scene."
  },
  {
    id: 132,
    title: "The Mystic Marriage of Saint Catherine",
    artist: "Hans Memling",
    year: "1479",
    url: "https://upload.wikimedia.org/wikipedia/commons/0/0d/Hans_Memling_-_Mystic_Marriage_of_St_Catherine_-_WGA14945.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Memling Museum, Bruges",
    description: "Sacred scene with detailed landscape background."
  },
  {
    id: 133,
    title: "Portrait of Baldassare Castiglione",
    artist: "Raphael",
    year: "1515",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/85/Baldassare_Castiglione%2C_by_Raffaello_Sanzio%2C_from_C2RMF_retouched.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Louvre Museum, Paris",
    description: "Portrait of the famous Renaissance author and diplomat."
  },
  {
    id: 134,
    title: "The Assumption of the Virgin",
    artist: "Francesco Botticini",
    year: "1475-1476",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5c/Francesco_Botticini_-_The_Assumption_of_the_Virgin.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "National Gallery, London",
    description: "Hierarchical composition of heavenly spheres."
  },
  {
    id: 135,
    title: "The Ghent Altarpiece (Open)",
    artist: "Jan van Eyck",
    year: "1432",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/53/Retable_de_l%27Agneau_mystique.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Saint Bavo's Cathedral, Ghent",
    description: "Masterpiece of Early Netherlandish painting."
  },
  {
    id: 136,
    title: "The Battle of Alexander at Issus",
    artist: "Albrecht Altdorfer",
    year: "1529",
    url: "https://upload.wikimedia.org/wikipedia/commons/e/e4/Albrecht_Altdorfer_-_The_Battle_of_Alexander_at_Issus_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Alte Pinakothek, Munich",
    description: "Dramatic battle scene with cosmic landscape."
  },
  {
    id: 137,
    title: "The Crucified Christ",
    artist: "Andrea Mantegna",
    year: "1459",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8b/Andrea_Mantegna_-_Christ_as_the_Suffering_Redeemer_-_WGA13981.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Louvre Museum, Paris",
    description: "Innovative perspective view of the crucified Christ."
  },
  {
    id: 138,
    title: "The Descent from the Cross",
    artist: "Rogier van der Weyden",
    year: "1435",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/1a/Descent_from_the_cross_-_Rogier_van_der_Weyden.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "Emotionally powerful depiction of Christ's deposition."
  },
  {
    id: 139,
    title: "The Meeting at the Golden Gate",
    artist: "Giotto",
    year: "1305",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/51/Giotto_-_Scrovegni_-_-06-_-_Meeting_at_the_Golden_Gate.jpg",
    period: periods.PROTO_RENAISSANCE,
    location: "Scrovegni Chapel, Padua",
    description: "Meeting of Joachim and Anna, parents of the Virgin Mary."
  },
  {
    id: 140,
    title: "The Adoration of the Mystic Lamb",
    artist: "Jan van Eyck",
    year: "1432",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9d/Jan_van_Eyck_-_The_Adoration_of_the_Mystic_Lamb.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Saint Bavo's Cathedral, Ghent",
    description: "Central panel of the Ghent Altarpiece."
  },
  {
    id: 141,
    title: "Portrait of a Man in a Red Turban",
    artist: "Jan van Eyck",
    year: "1433",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d7/Portrait_of_a_Man_by_Jan_van_Eyck-small.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Possibly a self-portrait of the artist."
  },
  {
    id: 142,
    title: "The Death of Actaeon",
    artist: "Titian",
    year: "1559-1575",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/98/Titian_-_The_Death_of_Actaeon_-_Google_Art_Project.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Mythological scene of Diana punishing Actaeon."
  },
  {
    id: 143,
    title: "The Flagellation of Christ",
    artist: "Piero della Francesca",
    year: "1455",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/11/Piero_della_Francesca_-_Flagellation_of_Christ_-_WGA17597.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Galleria Nazionale delle Marche, Urbino",
    description: "Masterpiece of Renaissance perspective and composition."
  },
  {
    id: 144,
    title: "The Fall of Icarus",
    artist: "Pieter Bruegel the Elder",
    year: "1558",
    url: "https://upload.wikimedia.org/wikipedia/commons/c/c2/Pieter_Bruegel_the_Elder_-_Landscape_with_the_Fall_of_Icarus_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Royal Museums of Fine Arts, Brussels",
    description: "Landscape where mythological event occurs almost unnoticed."
  },
  {
    id: 145,
    title: "The Battle of San Romano",
    artist: "Paolo Uccello",
    year: "1438-1440",
    url: "https://upload.wikimedia.org/wikipedia/commons/e/ec/Paolo_Uccello_-_The_Battle_of_San_Romano_-_Google_Art_Project.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "National Gallery, London",
    description: "Dynamic battle scene with experimental perspective."
  },
  {
    id: 146,
    title: "Portrait of a Young Woman",
    artist: "Rogier van der Weyden",
    year: "1440",
    url: "https://upload.wikimedia.org/wikipedia/commons/6/66/Rogier_van_der_Weyden_-_Portrait_of_a_Young_Woman_-_WGA25656.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Gemäldegalerie, Berlin",
    description: "Delicate portrait of unknown noblewoman."
  },
  {
    id: 147,
    title: "The Annunciation with Saint Emidius",
    artist: "Carlo Crivelli",
    year: "1486",
    url: "https://upload.wikimedia.org/wikipedia/commons/7/79/Carlo_Crivelli_007.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "National Gallery, London",
    description: "Complex architectural setting with detailed symbolism."
  },
  {
    id: 148,
    title: "The Hunters in the Snow",
    artist: "Pieter Bruegel the Elder",
    year: "1565",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d8/Pieter_Bruegel_the_Elder_-_Hunters_in_the_Snow_%28Winter%29_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Winter landscape showing return of hunters to village."
  },
  {
    id: 149,
    title: "Portrait of Sigismund",
    artist: "Albrecht Dürer",
    year: "1513",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9b/Albrecht_D%C3%BCrer_-_Emperor_Sigismund_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Germanisches Nationalmuseum, Nuremberg",
    description: "Portrait of Holy Roman Emperor Sigismund."
  },
  {
    id: 150,
    title: "The Finding of the True Cross",
    artist: "Piero della Francesca",
    year: "1460",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f5/Discovery_and_Proof_of_the_True_Cross%2C_Piero_della_Francesca.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Basilica of San Francesco, Arezzo",
    description: "Fresco depicting the legend of the True Cross."
  },
  {
    id: 151,
    title: "The Adoration of the Magi",
    artist: "Gentile da Fabriano",
    year: "1423",
    url: "https://upload.wikimedia.org/wikipedia/commons/7/7c/Gentile_da_Fabriano_001.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Ornate Gothic-style altarpiece with gold leaf details."
  },
  {
    id: 152,
    title: "The Portinari Altarpiece",
    artist: "Hugo van der Goes",
    year: "1475",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f7/Hugo_van_der_Goes_-_The_Portinari_Altarpiece%2C_Uffizi.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Influential Netherlandish triptych in Florence."
  },
  {
    id: 153,
    title: "Portrait of Federico da Montefeltro",
    artist: "Piero della Francesca",
    year: "1465",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d9/Piero_della_Francesca_-_Federico_da_Montefeltro_-_WGA17596.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Famous profile portrait of the Duke of Urbino."
  },
  {
    id: 154,
    title: "The Last Supper",
    artist: "Dirk Bouts",
    year: "1464-1468",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/31/Dirk_Bouts_-_The_Last_Supper_-_WGA03028.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "St. Peter's Church, Leuven",
    description: "Early example of single-point perspective in Northern art."
  },
  {
    id: 155,
    title: "The Triumph of Death",
    artist: "Pieter Bruegel the Elder",
    year: "1562",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/10/Pieter_Bruegel_the_Elder_-_The_Triumph_of_Death_-_WGA3393.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "Apocalyptic scene depicting death's victory over mortal affairs."
  },
  {
    id: 156,
    title: "Saint George and the Dragon",
    artist: "Paolo Uccello",
    year: "1470",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9a/Paolo_Uccello_047.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "National Gallery, London",
    description: "Dramatic portrayal of the legendary battle."
  },
  {
    id: 157,
    title: "The Garden of Paradise",
    artist: "Master of the Upper Rhine",
    year: "1410",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/84/Garden_of_paradise.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Städel Museum, Frankfurt",
    description: "Intimate scene of the Virgin and saints in an enclosed garden."
  },
  {
    id: 158,
    title: "The Miracle of the Relic of the Cross",
    artist: "Vittore Carpaccio",
    year: "1494",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5b/Vittore_Carpaccio_-_Miracle_of_the_Relic_of_the_Cross_at_the_Ponte_di_Rialto_-_WGA04334.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "Gallerie dell'Accademia, Venice",
    description: "Detailed view of Renaissance Venice during a miracle."
  },
  {
    id: 159,
    title: "The Madonna with Canon van der Paele",
    artist: "Jan van Eyck",
    year: "1434-1436",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d7/Jan_van_Eyck_-_Virgin_and_Child_with_Canon_van_der_Paele_-_WGA7620.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Groeningemuseum, Bruges",
    description: "Detailed donor portrait with religious figures."
  },
  {
    id: 160,
    title: "The Feast of the Gods",
    artist: "Giovanni Bellini",
    year: "1514",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8a/Giovanni_Bellini_and_Titian_-_The_Feast_of_the_Gods_-_Google_Art_Project.jpg",
    period: periods.VENETIAN_RENAISSANCE,
    location: "National Gallery of Art, Washington D.C.",
    description: "Mythological scene completed by Titian after Bellini's death."
  },
  {
    id: 161,
    title: "The Tower of Babel",
    artist: "Pieter Bruegel the Elder",
    year: "1563",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/fc/Pieter_Bruegel_the_Elder_-_The_Tower_of_Babel_%28Vienna%29_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Biblical story depicted as contemporary construction project."
  },
  {
    id: 162,
    title: "The Legend of Saint Lucy",
    artist: "Domenico Veneziano",
    year: "1445-1447",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/1b/Domenico_Veneziano_-_St_Lucy_Altarpiece_-_WGA06414.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Altarpiece depicting scenes from saint's life."
  },
  {
    id: 163,
    title: "Portrait of a Lady",
    artist: "Petrus Christus",
    year: "1470",
    url: "https://upload.wikimedia.org/wikipedia/commons/6/66/Petrus_Christus_-_Portrait_of_a_Young_Woman_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Gemäldegalerie, Berlin",
    description: "Elegant portrait showing Burgundian court fashion."
  },
  {
    id: 164,
    title: "The Battle of the Amazons",
    artist: "Hans Burgkmair",
    year: "1508",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/3e/Hans_Burgkmair_d._%C3%84._-_Amazonenschlacht_-_1508.jpeg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Alte Pinakothek, Munich",
    description: "Dynamic battle scene between Greeks and Amazons."
  },
  {
    id: 165,
    title: "The Healing of the Cripple",
    artist: "Masaccio",
    year: "1426",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/b2/Masaccio_-_St_Peter_Healing_the_Sick_with_his_Shadow_-_WGA14184.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Brancacci Chapel, Florence",
    description: "Fresco showing Saint Peter healing with his shadow."
  },
  {
    id: 166,
    title: "Christ and the Woman Taken in Adultery",
    artist: "Pieter Bruegel the Elder",
    year: "1565",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9d/Pieter_Bruegel_the_Elder_-_Christ_and_the_Woman_Taken_in_Adultery_-_WGA3496.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Courtauld Institute of Art, London",
    description: "Biblical scene set in contemporary Netherlands."
  },
  {
    id: 167,
    title: "The Crucifixion",
    artist: "Fra Angelico",
    year: "1442",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/b3/Fra_Angelico_-_Crucifixion_-_WGA00525.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Convent of San Marco, Florence",
    description: "Meditative fresco for monastic cell."
  },
  {
    id: 168,
    title: "The Money Changer and His Wife",
    artist: "Quentin Matsys",
    year: "1514",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f1/Quentin_Matsys_-_The_Money_Changer_and_His_Wife_-_WGA14281.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Louvre Museum, Paris",
    description: "Detailed scene of financial transaction with moral undertones."
  },
  {
    id: 169,
    title: "The Ambassadors",
    artist: "Hans Holbein the Younger",
    year: "1533",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/88/Hans_Holbein_the_Younger_-_The_Ambassadors_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Double portrait with symbolic objects and anamorphic skull."
  },
  {
    id: 170,
    title: "The Donne Triptych",
    artist: "Hans Memling",
    year: "1478",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/b4/Hans_Memling_-_Donne_Triptych_-_National_Gallery_London.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Triptych commissioned by Welsh patron Sir John Donne."
  },
  {
    id: 171,
    title: "Saint Sebastian",
    artist: "Andrea Mantegna",
    year: "1480",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8c/Andrea_Mantegna_-_St_Sebastian_-_WGA13975.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Louvre Museum, Paris",
    description: "Martyred saint depicted with classical architecture."
  },
  {
    id: 172,
    title: "The Peasant Wedding",
    artist: "Pieter Bruegel the Elder",
    year: "1567",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/b7/Pieter_Bruegel_the_Elder_-_Peasant_Wedding_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Lively scene of rural celebration."
  },
  {
    id: 173,
    title: "The Story of Nastagio degli Onesti",
    artist: "Sandro Botticelli",
    year: "1483",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Botticelli_-_Nastagio_degli_Onesti_-_First_Episode.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "Series depicting Boccaccio's supernatural tale."
  },
  {
    id: 174,
    title: "Self-Portrait",
    artist: "Albrecht Dürer",
    year: "1500",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/dc/Albrecht_D%C3%BCrer_-_Self-Portrait_%28Munich%29.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Alte Pinakothek, Munich",
    description: "Iconic frontal self-portrait in Christ-like pose."
  },
  {
    id: 175,
    title: "The Presentation in the Temple",
    artist: "Fra Angelico",
    year: "1440",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/3e/Fra_Angelico_-_Presentation_in_the_Temple_-_WGA00513.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museum of San Marco, Florence",
    description: "Biblical scene with architectural setting."
  },
  {
    id: 176,
    title: "Christ Carrying the Cross",
    artist: "Hieronymus Bosch",
    year: "1515",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/96/Hieronymus_Bosch_-_Christ_Carrying_the_Cross_-_WGA2513.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museum of Fine Arts, Ghent",
    description: "Grotesque faces surrounding suffering Christ."
  },
  {
    id: 177,
    title: "The Dormition of the Virgin",
    artist: "Andrea Mantegna",
    year: "1462",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9c/Andrea_Mantegna_-_The_Death_of_the_Virgin_-_Google_Art_Project.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "Death of Mary with dramatic foreshortening."
  },
  {
    id: 178,
    title: "The Garden of Earthly Delights (exterior)",
    artist: "Hieronymus Bosch",
    year: "1490-1510",
    url: "https://upload.wikimedia.org/wikipedia/commons/6/6d/The_Garden_of_Earthly_Delights_by_Bosch_High_Resolution.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "Exterior panels showing creation of the world."
  },
  {
    id: 179,
    title: "The Allegory of Good and Bad Government",
    artist: "Ambrogio Lorenzetti",
    year: "1338-1339",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9d/Ambrogio_Lorenzetti_-_Effects_of_Good_Government_in_the_city_-_Google_Art_Project.jpg",
    period: periods.PROTO_RENAISSANCE,
    location: "Palazzo Pubblico, Siena",
    description: "Political frescoes showing effects of governance."
  },
  {
    id: 180,
    title: "Portrait of a Young Man with an Apple",
    artist: "Hans Holbein the Younger",
    year: "1541",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d8/Hans_Holbein_the_Younger_-_Portrait_of_a_Young_Man_with_an_Apple_-_WGA11537.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Elegant portrait with symbolic fruit."
  },
  {
    id: 181,
    title: "The Arnolfini Portrait",
    artist: "Jan van Eyck",
    year: "1434",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/33/Van_Eyck_-_Arnolfini_Portrait.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "National Gallery, London",
    description: "Famous double portrait with complex symbolism."
  },
  {
    id: 182,
    title: "The Last Judgment",
    artist: "Stefan Lochner",
    year: "1435",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/3a/Stefan_Lochner_-_Last_Judgement_-_WGA13332.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Wallraf-Richartz Museum, Cologne",
    description: "Detailed scene of final judgment with paradise and hell."
  },
{
    id: 183,
    title: "The Seven Deadly Sins",
    artist: "Hieronymus Bosch",
    year: "1485",
    url: "https://upload.wikimedia.org/wikipedia/commons/2/2a/Hieronymus_Bosch-_The_Seven_Deadly_Sins_and_the_Four_Last_Things.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "Circular tabletop painting depicting moral allegories."
  },
  {
    id: 184,
    title: "The Descent from the Cross",
    artist: "Rogier van der Weyden",
    year: "1435",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/1a/Descent_from_the_cross_-_Rogier_van_der_Weyden.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Museo del Prado, Madrid",
    description: "Emotionally powerful depiction of Christ's deposition."
  },
  {
    id: 185,
    title: "The Battle of Alexander at Issus",
    artist: "Albrecht Altdorfer",
    year: "1529",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f3/Albrecht_Altdorfer_-_The_Battle_of_Alexander_at_Issus_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Alte Pinakothek, Munich",
    description: "Dramatic cosmic view of ancient battle."
  },
  {
    id: 186,
    title: "The Ghent Altarpiece (Closed)",
    artist: "Hubert and Jan van Eyck",
    year: "1432",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9d/Ghent_Altarpiece_closed.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Saint Bavo Cathedral, Ghent",
    description: "Exterior panels of the famous polyptych."
  },
  {
    id: 187,
    title: "The Madonna of Chancellor Rolin",
    artist: "Jan van Eyck",
    year: "1435",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d0/Jan_van_Eyck_-_The_Virgin_of_Chancellor_Rolin_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Louvre Museum, Paris",
    description: "Donor portrait with detailed cityscape background."
  },
  {
    id: 188,
    title: "The Crucifixion of Saint Peter",
    artist: "Masaccio",
    year: "1426",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/b4/Masaccio_-_Crucifixion_of_St_Peter_-_WGA14187.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Brancacci Chapel, Florence",
    description: "Revolutionary fresco showing dramatic martyrdom."
  },
  {
    id: 189,
    title: "The Temptation of Saint Anthony",
    artist: "Martin Schongauer",
    year: "1470-1475",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8a/Martin_Schongauer_-_The_Temptation_of_St_Anthony_-_WGA21033.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Various Collections",
    description: "Influential engraving of saint's torment."
  },
  {
    id: 190,
    title: "The Legend of Saint Ursula",
    artist: "Hans Memling",
    year: "1489",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/55/Hans_Memling_-_Scenes_from_the_Life_of_Saint_Ursula_-_WGA14940.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Memling Museum, Bruges",
    description: "Narrative cycle on elaborate reliquary."
  },
  {
    id: 191,
    title: "The Adoration of the Mystic Lamb",
    artist: "Hubert and Jan van Eyck",
    year: "1432",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5c/Retable_de_l%27Agneau_mystique.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Saint Bavo Cathedral, Ghent",
    description: "Central panel of Ghent Altarpiece."
  },
  {
    id: 192,
    title: "The Garden of Love",
    artist: "Master of the Garden of Paradise",
    year: "1410-1420",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/84/Garden_of_paradise.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Städel Museum, Frankfurt",
    description: "Courtly scene in enclosed garden setting."
  },
  {
    id: 193,
    title: "The Beheading of Saint John the Baptist",
    artist: "Giovanni di Paolo",
    year: "1455-1460",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/1b/Giovanni_di_Paolo_-_The_Head_of_Saint_John_the_Baptist_Brought_to_Herod_-_Google_Art_Project.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Art Institute of Chicago",
    description: "Dramatic scene of martyrdom with Gothic elements."
  },
  {
    id: 194,
    title: "Portrait of a Man with a Pink",
    artist: "Hans Memling",
    year: "1480",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d4/Hans_Memling_-_Man_with_a_Pink_-_WGA14947.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Thyssen-Bornemisza Museum, Madrid",
    description: "Intimate portrait with symbolic flower."
  },
  {
    id: 195,
    title: "The Carrying of the Cross",
    artist: "Hieronymus Bosch",
    year: "1490",
    url: "https://upload.wikimedia.org/wikipedia/commons/4/46/Jheronimus_Bosch_-_Christ_carrying_the_Cross_%28Vienna%29_-_Google_Art_Project.jpg",
    period: periods.NORTHERN_RENAISSANCE,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Grotesque crowd surrounding suffering Christ."
  },
  {
    id: 196,
    title: "Portrait of a Lady in Green",
    artist: "Agnolo Bronzino",
    year: "1530-1532",
    url: "https://upload.wikimedia.org/wikipedia/commons/d/d5/Angelo_Bronzino_-_Portrait_of_a_Lady_in_Green_-_WGA3247.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Royal Collection, Windsor Castle",
    description: "Elegant Mannerist portrait of noblewoman."
  },
// Continuing the more Artworks array, now including sculptures...

  {
    id: 197,
    title: "David",
    artist: "Michelangelo",
    year: "1501-1504",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/80/Michelangelo%27s_David_-_right_view_2.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Galleria dell'Accademia, Florence",
    description: "Monumental marble statue of biblical hero David.",
    type: "sculpture"
  },
  {
    id: 198,
    title: "Pietà",
    artist: "Michelangelo",
    year: "1498-1499",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/1f/Michelangelo%27s_Pieta_5450_cut_out_black.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "St. Peter's Basilica, Vatican City",
    description: "Marble sculpture depicting Mary holding dead Christ.",
    type: "sculpture"
  },
  {
    id: 199,
    title: "David",
    artist: "Donatello",
    year: "1440-1443",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8e/Donatello_-_David_-_Bargello.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museo Nazionale del Bargello, Florence",
    description: "Bronze statue of David, first free-standing nude since antiquity.",
    type: "sculpture"
  },
  {
    id: 200,
    title: "Mary Magdalene",
    artist: "Donatello",
    year: "1455",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/b1/Donatello%2C_maria_maddalena_01.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museo dell'Opera del Duomo, Florence",
    description: "Wooden sculpture showing penitent saint.",
    type: "sculpture"
  },
  {
    id: 201,
    title: "Judith and Holofernes",
    artist: "Donatello",
    year: "1457-1464",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8e/Judith_and_Holofernes_by_Donatello_-_Palazzo_Vecchio_-_Florence_2016.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Palazzo Vecchio, Florence",
    description: "Bronze depicting biblical heroine's triumph.",
    type: "sculpture"
  },
  {
    id: 202,
    title: "Perseus with the Head of Medusa",
    artist: "Benvenuto Cellini",
    year: "1545-1554",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/96/Persee_de_Cellini_Florence.jpg",
    period: periods.MANNERISM,
    location: "Loggia dei Lanzi, Florence",
    description: "Bronze masterpiece of Mannerist sculpture.",
    type: "sculpture"
  },
  {
    id: 203,
    title: "The Prophet Habakkuk",
    artist: "Donatello",
    year: "1423-1435",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8e/Habacuc_donatello.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museo dell'Opera del Duomo, Florence",
    description: "Marble statue known as 'Lo Zuccone' (The Pumpkin Head).",
    type: "sculpture"
  },
  {
    id: 204,
    title: "Equestrian Monument of Gattamelata",
    artist: "Donatello",
    year: "1453",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/37/Monumento_equestre_al_Gattamelata_02.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Piazza del Santo, Padua",
    description: "First major bronze equestrian monument since antiquity.",
    type: "sculpture"
  },
  {
    id: 205,
    title: "Moses",
    artist: "Michelangelo",
    year: "1513-1515",
    url: "https://upload.wikimedia.org/wikipedia/commons/7/7c/Moses_by_Michelangelo_in_San_Pietro_in_Vincoli.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "San Pietro in Vincoli, Rome",
    description: "Marble statue for Pope Julius II's tomb.",
    type: "sculpture"
  },
  {
    id: 206,
    title: "The Singing Gallery (Cantoria)",
    artist: "Luca della Robbia",
    year: "1431-1438",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Cantoria_di_luca_della_robbia_02.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museo dell'Opera del Duomo, Florence",
    description: "Marble reliefs showing musical celebration.",
    type: "sculpture"
  },
  {
    id: 207,
    title: "Tomb of Ilaria del Carretto",
    artist: "Jacopo della Quercia",
    year: "1406-1408",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/98/Jacopo_della_quercia%2C_monumento_funebre_di_ilaria_del_carretto_02.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Cathedral of San Martino, Lucca",
    description: "Marble tomb with reclining effigy.",
    type: "sculpture"
  },
  {
    id: 208,
    title: "St. John the Baptist",
    artist: "Lorenzo Ghiberti",
    year: "1412-1416",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Lorenzo_ghiberti%2C_san_giovanni_battista%2C_1412-16%2C_01.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Orsanmichele, Florence",
    description: "Bronze statue for guild niche.",
    type: "sculpture"
  },
  {
    id: 209,
    title: "Gates of Paradise",
    artist: "Lorenzo Ghiberti",
    year: "1425-1452",
    url: "https://upload.wikimedia.org/wikipedia/commons/c/c8/Gates_of_Paradise_Florence_Baptistry_Lorenzo_Ghiberti_1425-52.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Baptistery of San Giovanni, Florence",
    description: "Gilt bronze doors with biblical reliefs.",
    type: "sculpture"
  },
  {
    id: 210,
    title: "Bust of Niccolò da Uzzano",
    artist: "Donatello",
    year: "1432",
    url: "https://upload.wikimedia.org/wikipedia/commons/4/47/Donatello%2C_niccol%C3%B2_da_uzzano_01.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Bargello National Museum, Florence",
    description: "Painted terracotta portrait bust.",
    type: "sculpture"
  },
  {
    id: 197,
    title: "David",
    artist: "Michelangelo",
    year: "1501-1504",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/80/Michelangelo%27s_David_-_right_view_2.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Galleria dell'Accademia, Florence",
    description: "Monumental marble statue of biblical hero David.",
    type: "sculpture"
  },
  {
    id: 198,
    title: "Pietà",
    artist: "Michelangelo",
    year: "1498-1499",
    url: "https://upload.wikimedia.org/wikipedia/commons/1/1f/Michelangelo%27s_Pieta_5450_cut_out_black.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "St. Peter's Basilica, Vatican City",
    description: "Marble sculpture depicting Mary holding dead Christ.",
    type: "sculpture"
  },
  {
    id: 199,
    title: "David",
    artist: "Donatello",
    year: "1440-1443",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8e/Donatello_-_David_-_Bargello.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museo Nazionale del Bargello, Florence",
    description: "Bronze statue of David, first free-standing nude since antiquity.",
    type: "sculpture"
  },
  {
    id: 200,
    title: "Mary Magdalene",
    artist: "Donatello",
    year: "1455",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/b1/Donatello%2C_maria_maddalena_01.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museo dell'Opera del Duomo, Florence",
    description: "Wooden sculpture showing penitent saint.",
    type: "sculpture"
  },
  {
    id: 201,
    title: "Judith and Holofernes",
    artist: "Donatello",
    year: "1457-1464",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8e/Judith_and_Holofernes_by_Donatello_-_Palazzo_Vecchio_-_Florence_2016.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Palazzo Vecchio, Florence",
    description: "Bronze depicting biblical heroine's triumph.",
    type: "sculpture"
  },
  {
    id: 202,
    title: "Perseus with the Head of Medusa",
    artist: "Benvenuto Cellini",
    year: "1545-1554",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/96/Persee_de_Cellini_Florence.jpg",
    period: periods.MANNERISM,
    location: "Loggia dei Lanzi, Florence",
    description: "Bronze masterpiece of Mannerist sculpture.",
    type: "sculpture"
  },
  {
    id: 203,
    title: "The Prophet Habakkuk",
    artist: "Donatello",
    year: "1423-1435",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8e/Habacuc_donatello.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museo dell'Opera del Duomo, Florence",
    description: "Marble statue known as 'Lo Zuccone' (The Pumpkin Head).",
    type: "sculpture"
  },
  {
    id: 204,
    title: "Equestrian Monument of Gattamelata",
    artist: "Donatello",
    year: "1453",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/37/Monumento_equestre_al_Gattamelata_02.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Piazza del Santo, Padua",
    description: "First major bronze equestrian monument since antiquity.",
    type: "sculpture"
  },
  {
    id: 205,
    title: "Moses",
    artist: "Michelangelo",
    year: "1513-1515",
    url: "https://upload.wikimedia.org/wikipedia/commons/7/7c/Moses_by_Michelangelo_in_San_Pietro_in_Vincoli.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "San Pietro in Vincoli, Rome",
    description: "Marble statue for Pope Julius II's tomb.",
    type: "sculpture"
  },
  {
    id: 206,
    title: "The Singing Gallery (Cantoria)",
    artist: "Luca della Robbia",
    year: "1431-1438",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Cantoria_di_luca_della_robbia_02.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Museo dell'Opera del Duomo, Florence",
    description: "Marble reliefs showing musical celebration.",
    type: "sculpture"
  },
  {
    id: 207,
    title: "Tomb of Ilaria del Carretto",
    artist: "Jacopo della Quercia",
    year: "1406-1408",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/98/Jacopo_della_quercia%2C_monumento_funebre_di_ilaria_del_carretto_02.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Cathedral of San Martino, Lucca",
    description: "Marble tomb with reclining effigy.",
    type: "sculpture"
  },
  {
    id: 208,
    title: "St. John the Baptist",
    artist: "Lorenzo Ghiberti",
    year: "1412-1416",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Lorenzo_ghiberti%2C_san_giovanni_battista%2C_1412-16%2C_01.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Orsanmichele, Florence",
    description: "Bronze statue for guild niche.",
    type: "sculpture"
  },
  {
    id: 209,
    title: "Gates of Paradise",
    artist: "Lorenzo Ghiberti",
    year: "1425-1452",
    url: "https://upload.wikimedia.org/wikipedia/commons/c/c8/Gates_of_Paradise_Florence_Baptistry_Lorenzo_Ghiberti_1425-52.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Baptistery of San Giovanni, Florence",
    description: "Gilt bronze doors with biblical reliefs.",
    type: "sculpture"
  },
  {
    id: 210,
    title: "Bust of Niccolò da Uzzano",
    artist: "Donatello",
    year: "1432",
    url: "https://upload.wikimedia.org/wikipedia/commons/4/47/Donatello%2C_niccol%C3%B2_da_uzzano_01.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Bargello National Museum, Florence",
    description: "Painted terracotta portrait bust.",
    type: "sculpture"
  },
  {
    id: 224,
    title: "Tomb of Leonardo Bruni",
    artist: "Bernardo Rossellino",
    year: "1444-1450",
    url: "https://upload.wikimedia.org/wikipedia/commons/0/0f/Bernardo_rossellino%2C_monumento_funebre_di_leonardo_bruni.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Santa Croce, Florence",
    description: "Marble wall tomb of humanist scholar.",
    type: "sculpture"
  },
  {
    id: 225,
    title: "Medici Madonna",
    artist: "Michelangelo",
    year: "1521-1534",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8f/Michelangelo%2C_madonna_medici.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Medici Chapel, Florence",
    description: "Marble Madonna and Child for Medici tombs.",
    type: "sculpture"
  },
  {
    id: 226,
    title: "Bust of Filippo Strozzi",
    artist: "Benedetto da Maiano",
    year: "1475",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f2/Benedetto_da_maiano%2C_busto_di_filippo_strozzi.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Louvre Museum, Paris",
    description: "Marble portrait of Florentine banker.",
    type: "sculpture"
  },
  {
    id: 227,
    title: "Tomb of Antipope John XXIII",
    artist: "Donatello and Michelozzo",
    year: "1422-1428",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9d/Donatello_e_michelozzo%2C_monumento_dell%27antipapa_giovanni_XXIII.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Baptistery of Florence",
    description: "Bronze and marble wall tomb.",
    type: "sculpture"
  },
  {
    id: 228,
    title: "Bust of Pietro de' Medici",
    artist: "Mino da Fiesole",
    year: "1453",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Mino_da_fiesole%2C_busto_di_piero_di_cosimo_de%27_medici.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Bargello National Museum, Florence",
    description: "Marble portrait of Medici patron.",
    type: "sculpture"
  },
  {
    id: 229,
    title: "Tomb of Mary of Hungary",
    artist: "Tino di Camaino",
    year: "1325",
    url: "https://upload.wikimedia.org/wikipedia/commons/a/a9/Tino_di_Camaino_tomb_Mary_of_Hungary.jpg",
    period: periods.PROTO_RENAISSANCE,
    location: "Santa Maria Donnaregina, Naples",
    description: "Gothic-Renaissance transitional tomb.",
    type: "sculpture"
  },
  {
    id: 230,
    title: "Hercules and Antaeus",
    artist: "Antonio del Pollaiuolo",
    year: "1475",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8d/Pollaiuolo%2C_ercole_e_anteo_02.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Bargello National Museum, Florence",
    description: "Bronze statuette of mythological combat.",
    type: "sculpture"
  },
  {
    id: 231,
    title: "Relief of the Nativity",
    artist: "Donatello",
    year: "1460",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Donatello%2C_natività%2C_1460_circa.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Santa Maria del Carmine, Padua",
    description: "Bronze relief with revolutionary perspective.",
    type: "sculpture"
  },
  {
    id: 232,
    title: "Bust of Christ",
    artist: "Tullio Lombardo",
    year: "1500-1505",
    url: "https://upload.wikimedia.org/wikipedia/commons/4/4f/Tullio_lombardo%2C_busto_di_cristo.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Galleria Giorgio Franchetti, Venice",
    description: "Marble portrait of idealized Christ.",
    type: "sculpture"
  },
  {
    id: 233,
    title: "Tomb of Doge Andrea Vendramin",
    artist: "Tullio Lombardo",
    year: "1493-1499",
    url: "https://upload.wikimedia.org/wikipedia/commons/6/6f/Monumento_al_doge_Andrea_Vendramin.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Santi Giovanni e Paolo, Venice",
    description: "Elaborate marble ducal tomb.",
    type: "sculpture"
  },
  {
    id: 234,
    title: "Adam",
    artist: "Tullio Lombardo",
    year: "1490-1495",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Tullio_Lombardo_Adam.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Metropolitan Museum of Art, New York",
    description: "Classical nude representing first man.",
    type: "sculpture"
  },
  {
    id: 235,
    title: "Tomb of Marsilio Ficino",
    artist: "Andrea di Piero Ferrucci",
    year: "1521",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f8/Tomb_of_Marsilio_Ficino.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Florence Cathedral",
    description: "Wall tomb of Neoplatonic philosopher.",
    type: "sculpture"
  },
  {
    id: 236,
    title: "Venus and Cupid",
    artist: "Jacopo Sansovino",
    year: "1550",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/3f/Jacopo_sansovino%2C_venere_e_cupido.jpg",
    period: periods.MANNERISM,
    location: "Bargello National Museum, Florence",
    description: "Marble group showing goddess with son.",
    type: "sculpture"
  },
  {
    id: 237,
    title: "Sleeping Ariadne",
    artist: "Jacopo Sansovino",
    year: "1510",
    url: "https://upload.wikimedia.org/wikipedia/commons/6/6f/Jacopo_sansovino%2C_arianna_dormiente.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Uffizi Gallery, Florence",
    description: "Marble reclining figure of mythological heroine.",
    type: "sculpture"
  },
  {
    id: 238,
    title: "Bust of Costanza Bonarelli",
    artist: "Gian Lorenzo Bernini",
    year: "1636-1638",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/b1/Bust_of_Costanza_Bonarelli_by_Bernini.jpg",
    period: periods.LATE_RENAISSANCE,
    location: "Bargello National Museum, Florence",
    description: "Marble portrait of artist's mistress.",
    type: "sculpture"
  },
  {
    id: 239,
    title: "Madonna of the Stairs",
    artist: "Michelangelo",
    year: "1491",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/89/Michelangelo%2C_madonna_della_scala.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Casa Buonarroti, Florence",
    description: "Early marble relief showing technical mastery.",
    type: "sculpture"
  },
  {
    id: 240,
    title: "Battle of the Centaurs",
    artist: "Michelangelo",
    year: "1492",
    url: "https://upload.wikimedia.org/wikipedia/commons/7/74/Michelangelo%2C_battaglia_dei_centauri_02.jpg",
    period: periods.HIGH_RENAISSANCE,
    location: "Casa Buonarroti, Florence",
    description: "Early relief showing mythological battle.",
    type: "sculpture"
  },
  {
    id: 241,
    title: "Bust of Giuliano de' Medici",
    artist: "Alessandro Algardi",
    year: "1640-1645",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f8/Alessandro_algardi%2C_busto_di_giuliano_de%27_medici.jpg",
    period: periods.LATE_RENAISSANCE,
    location: "Bargello National Museum, Florence",
    description: "Marble portrait of Medici duke.",
    type: "sculpture"
  },
  {
    id: 242,
    title: "Mercury",
    artist: "Giambologna",
    year: "1580",
    url: "https://upload.wikimedia.org/wikipedia/commons/4/4c/Giambologna_mercury.jpg",
    period: periods.MANNERISM,
    location: "Bargello National Museum, Florence",
    description: "Bronze figure of flying messenger god.",
    type: "sculpture"
  },
  {
    id: 243,
    title: "The Rape of the Sabine Women",
    artist: "Giambologna",
    year: "1574-1582",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9d/Giambologna_sabine.jpg",
    period: periods.MANNERISM,
    location: "Loggia dei Lanzi, Florence",
    description: "Marble group showing dramatic multi-figure composition.",
    type: "sculpture"
  },
  {
    id: 244,
    title: "Neptune Fountain",
    artist: "Bartolomeo Ammannati",
    year: "1563-1565",
    url: "https://upload.wikimedia.org/wikipedia/commons/4/44/Fountain_of_Neptune_Florence.jpg",
    period: periods.MANNERISM,
    location: "Piazza della Signoria, Florence",
    description: "Monumental marble and bronze fountain.",
    type: "sculpture"
  },
  {
    id: 245,
    title: "Hercules and Cacus",
    artist: "Baccio Bandinelli",
    year: "1525-1534",
    url: "https://upload.wikimedia.org/wikipedia/commons/7/7b/Hercules_and_Cacus_Bandinelli_Florence.jpg",
    period: periods.MANNERISM,
    location: "Piazza della Signoria, Florence",
    description: "Marble group showing mythological combat.",
    type: "sculpture"
  },
  {
    id: 246,
    title: "Flying Mercury",
    artist: "Giambologna",
    year: "1564-1580",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/33/Giambologna_Mercury.jpg",
    period: periods.MANNERISM,
    location: "Kunsthistorisches Museum, Vienna",
    description: "Bronze figure balanced on breath of wind.",
    type: "sculpture"
  },
  {
    id: 247,
    title: "Samson and the Philistine",
    artist: "Giambologna",
    year: "1561-1562",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/9a/Samson_slaying_a_philistine_giambologna.jpg",
    period: periods.MANNERISM,
    location: "Victoria and Albert Museum, London",
    description: "Dramatic marble group showing biblical combat.",
    type: "sculpture"
  },
  {
    id: 248,
    title: "Architecture",
    artist: "Giovanni da Bologna",
    year: "1565",
    url: "https://upload.wikimedia.org/wikipedia/commons/f/f7/Giambologna%2C_architettura.jpg",
    period: periods.MANNERISM,
    location: "Museo Nazionale del Bargello, Florence",
    description: "Allegorical female figure in marble.",
    type: "sculpture"
  },
  {
    id: 249,
    title: "Bust of Bindo Altoviti",
    artist: "Benvenuto Cellini",
    year: "1549",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Benvenuto_cellini%2C_busto_di_bindo_altoviti.jpg",
    period: periods.MANNERISM,
    location: "Isabella Stewart Gardner Museum, Boston",
    description: "Bronze portrait of Florentine banker.",
    type: "sculpture"
  },
  {
    id: 250,
    title: "Perseus with the Head of Medusa",
    artist: "Benvenuto Cellini",
    year: "1545-1554",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/96/Perseo_di_Benvenuto_Cellini_2019.jpg",
    period: periods.MANNERISM,
    location: "Loggia dei Lanzi, Florence",
    description: "Bronze masterpiece showing hero with slain Gorgon.",
    type: "sculpture"
  },
  {
    id: 251,
    title: "Charity",
    artist: "Andrea del Verrocchio",
    year: "1469",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/b8/Andrea_del_verrocchio%2C_carità.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Bargello National Museum, Florence",
    description: "Allegorical terracotta figure with children.",
    type: "sculpture"
  },
  {
    id: 252,
    title: "Apollo and Daphne",
    artist: "Antonio del Pollaiuolo",
    year: "1470-1480",
    url: "https://upload.wikimedia.org/wikipedia/commons/3/3f/Apollo_and_Daphne_Pollaiuolo.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "National Gallery of Art, Washington D.C.",
    description: "Bronze statuette of mythological transformation.",
    type: "sculpture"
  },
  {
    id: 253,
    title: "Tomb of Ilaria del Carretto",
    artist: "Jacopo della Quercia",
    year: "1406-1408",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Jacopo_della_quercia%2C_monumento_funebre_di_ilaria_del_carretto_02.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Cathedral of San Martino, Lucca",
    description: "Marble tomb with reclining effigy.",
    type: "sculpture"
  },
  {
    id: 254,
    title: "Bust of Niccolò da Uzzano",
    artist: "Donatello",
    year: "1432",
    url: "https://upload.wikimedia.org/wikipedia/commons/9/98/Donatello%2C_busto_di_niccolò_da_uzzano.jpg",
    period: periods.EARLY_RENAISSANCE,
    location: "Bargello National Museum, Florence",
    description: "Painted terracotta portrait of Florentine statesman.",
    type: "sculpture"
  }
];







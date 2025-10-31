import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.virheellinen = Varasto(-1, -1)
        self.varasto2 = Varasto(10, 20)

    def test_konstruktori_luo_tayden_varaston(self):
        self.assertAlmostEqual(self.varasto2.saldo, 10)

    def test_negatiivisesta_tilavuudesta_tyhja_varasto(self):
        self.assertAlmostEqual(self.virheellinen.tilavuus, 0)

    def test_negatiivisesta_saldosta_tyhja_varasto(self):
        self.assertAlmostEqual(self.virheellinen.saldo, 0)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivinen_lisays_ei_vaikuta(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_lisaus_ei_mene_yli(self):
        self.varasto.lisaa_varastoon(30)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivinen_ottaminen_ei_vaikuta(self):
        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_ottaminen_ei_mene_ali(self):
        self.varasto.lisaa_varastoon(1)
        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 1)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_merkkijonoesitys_oikein(self):
        self.varasto.lisaa_varastoon(3)

        mj = str(self.varasto)

        self.assertEqual(mj, "saldo = 3, vielä tilaa 7")

from jsonclass import Json
import numpy 
import matplotlib.pyplot as plt
class r:
    def __init__(self) -> None:
        self.btc = self.get_candles('btcusdt.txt')
        self.voo = self.get_candles('return~VOO.txt')['candles']
    @staticmethod
    def get_candles(file):
        j = Json(file)
        return j.readKey()
    
    def main(self):
        voo,btc = self.normalize()
        voo_close = self.get_close(voo,'close')
        btc_close = self.get_close(btc,4)
        r = numpy.corrcoef(voo_close, btc_close)[0, 1]
        return r

    def normalize(self):
        if len(self.voo) > len(self.btc):
            voo = self.normalize_list(self.voo,len(self.btc))
            btc = self.btc

        else:
            voo = self.voo
            btc = self.normalize_list(self.btc,len(self.voo))
        return voo,btc
    
    def normalize_list(self,candles,length):
        return candles[-length:]
    
    def get_close(self,candle_list,key):
        candle_list = [float(x[key]) for x in candle_list]
        return candle_list
        
if __name__ == '__main__':
    m = r()
    m.main()

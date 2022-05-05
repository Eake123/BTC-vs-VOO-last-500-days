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
        voo_close,btc_close = self.get_close(voo,btc)
        r = numpy.corrcoef(voo_close, btc_close)[0, 1]
        return r

    def normalize(self):
        if len(self.voo) > len(self.btc):
            voo = self.normalize_list(self.voo,len(self.btc))
            btc = self.normalize_list(self.btc,False)

        else:
            voo = self.normalize_list(self.voo,False)
            btc = self.normalize_list(self.btc,len(self.voo))
        return voo,btc
    
    def normalize_list(self,candles,length):
        if isinstance(length,int):
            return candles[-length:]
        else:
            return candles
    
    def get_close(self,first,second):
        first = [float(x['close']) for x in first]
        second = [float(x[4]) for x in second]
        return first,second
        
if __name__ == '__main__':
    m = r()
    m.main()
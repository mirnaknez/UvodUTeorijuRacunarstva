import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class SimEnka {
    
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String ulazniNiz = br.readLine().trim();
        List<String> lista = Arrays.asList(ulazniNiz.split("\\|"));
        List<List<String>> listaUlaznihZnakova = new LinkedList<>();
        for (String s : lista) {
        	listaUlaznihZnakova.add(Arrays.asList(s.split(",")));
        }
        
        String skupStanja = br.readLine().trim();
        List<String> listaStanja = Arrays.asList(skupStanja.split(","));
        
        String skupSimbola = br.readLine().trim();
        List<String> listaSimbola = Arrays.asList(skupSimbola.split(","));
        
        String skupPrihStanja = br.readLine().trim();
        List<String> listaPrihStanja = Arrays.asList(skupPrihStanja.split(","));
        
        String pocetnoStanje = br.readLine().trim();
        String izraz = null;
        String prijasnjiizraz = null;
        
        Map<List<String>, List<String>> fjePrijelaza = new HashMap<>();
        
        try {
        	while((izraz = br.readLine()) != null) {
        		if(izraz.equals("")) {
        			break;
        		}
    			List<String> lista2 = new LinkedList<>(List.of(izraz.trim().split("->")));
    			List<String> stanja1 = new LinkedList<>(List.of(lista2.get(0).split(",")));
    			List<String> stanja2 = new LinkedList<>(List.of(lista2.get(1).split(",")));
    				
    			boolean provjera = false;
    			for(String s : stanja2) {
    				if(s.equals("#")) {
    					provjera = true;
    				}
    			}
    			if(!provjera) {
    				fjePrijelaza.put(stanja1, stanja2);
    			}
    			prijasnjiizraz = izraz;
    		}
        } catch (IndexOutOfBoundsException e){
        	System.out.print(e);
        }
        
        for(List<String> ulazniNizovi : listaUlaznihZnakova) {
        	Set<String> okolina = new TreeSet<>();
            Set<String> prethodnaokolina = new TreeSet<>();
        	prethodnaokolina.add(pocetnoStanje);
        	while(!prethodnaokolina.isEmpty()) {
    			Set<String> novaOkolina = new HashSet<>();
    			for(String stanje : prethodnaokolina) {
    				for(Map.Entry<List<String>, List<String>> set : fjePrijelaza.entrySet()) {
    					if(set.getKey().get(0).equals(stanje) && set.getKey().get(1).equals("$")) {
    						for(String s : set.getValue()) {
    							if(!prethodnaokolina.contains(s)) {
    								novaOkolina.add(s);
    							}
    						}
    					}
    				}
    			}
    			if(novaOkolina.isEmpty()) {
    				break;
    			}
    			else {
    				prethodnaokolina.addAll(novaOkolina);
    			}
    		}
        	int j = 1;
        	for(String jao : prethodnaokolina) {
    			System.out.print(jao);
    			if(j++ < prethodnaokolina.size()) {
    				System.out.print(",");
    			}
    		}
        	for(String trenutniPrijelaz : ulazniNizovi) {
        		for(String prethodnoStanje : prethodnaokolina) {
        			for(Map.Entry<List<String>, List<String>> set : fjePrijelaza.entrySet()) {
        				if(set.getKey().get(0).equals(prethodnoStanje) && set.getKey().get(1).equals(trenutniPrijelaz)) {
        					for(String stanje : set.getValue()) {
        						okolina.add(stanje);
        					}
        				}
        			}
        		}
        		if(okolina.isEmpty()) {
    				okolina.add("#");
        		}
        		while(!okolina.isEmpty()) {
        			Set<String> novaOkolina = new HashSet<>();
        			for(String stanje : okolina) {
        				for(Map.Entry<List<String>, List<String>> set : fjePrijelaza.entrySet()) {
        					if(set.getKey().get(0).equals(stanje) && set.getKey().get(1).equals("$")) {
        						for(String s : set.getValue()) {
        							if(!okolina.contains(s)) {
        								novaOkolina.add(s);
        							}
        						}
        					}
        				}
        			}
        			if(novaOkolina.isEmpty()) {
        				break;
        			}
        			else {
        				okolina.addAll(novaOkolina);
        			}
        		}
        		System.out.print("|");
        		int i = 1;
        		for(String jao : okolina) {
        			System.out.print(jao);
        			if(i++ < okolina.size()) {
        				System.out.print(",");
        			}
        		}
        		prethodnaokolina.clear();
        		prethodnaokolina.addAll(okolina);
        		okolina.clear();
        	}
    		System.out.print("\n");
        }
    }
	
    
}

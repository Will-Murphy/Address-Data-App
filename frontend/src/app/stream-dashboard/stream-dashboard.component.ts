import { Component, OnInit, Input } from '@angular/core';

import { HttpClient, HttpParams } from '@angular/common/http';
import { API_URL } from '../../environments/environment'; 

@Component({
  selector: 'app-stream-dashboard',
  templateUrl: './stream-dashboard.component.html',
  styleUrls: ['./stream-dashboard.component.css']
})
export class StreamDashboardComponent implements OnInit {

  //coordinate reverse geocoding state
  addressLat: number; 
  addressLong: number; 
  revGeocodeOutput: string;
  
  // address validation state 
  validationInput: string;
  validationOutput: string;

  // address geocoding state 
  geocodeInput: string;
  geocodeOutput: string; 

  constructor( private http: HttpClient) { }

  ngOnInit(): void {
  }

  validateAddress(address:string): string {
    this.validationInput = address
    const options = {
      responseType: 'text' as const, 
      params: new HttpParams().set('address', address)
    };
    
    const res = this.http.get(`${API_URL}/validate`, options).subscribe( 
                data =>  this.validationOutput = data
    );
    return this.validationOutput
  }

  geocodeAddress(address:string): string {
    this.geocodeInput = address
    const options = {
      responseType: 'text' as const, 
      params: new HttpParams().set('address', address)
    };
    
    const res = this.http.get(`${API_URL}/geocode`, options).subscribe( 
                data =>  this.geocodeOutput= data
    );
    return this.geocodeOutput
  }

  reverseGeocodeAddress(lat:number, long:number): string { 
    this.addressLat = lat 
    this.addressLong = long
    const coordinateString = `${lat},${long}`
    const options = {
      responseType: 'text' as const, 
      params: new HttpParams().set('coordinates', coordinateString)
    };
    
    const res = this.http.get(`${API_URL}/reverse-geocode`, options).subscribe( 
                data =>  this.revGeocodeOutput= data
    );
    return this.revGeocodeOutput
  }

}

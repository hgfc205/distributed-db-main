import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { addr } from "../environment/env";

const ip = addr;

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  headers = new HttpHeaders({ 'Content-Type': 'application/json; charset=utf-8' });

  constructor(private http: HttpClient) { }

  getCalls(data: any): Observable<any[]> {
    const url = `${ip}/calls_d`;
    return this.http.post<any[]>(url, JSON.stringify(data), { headers: this.headers });
  }
}

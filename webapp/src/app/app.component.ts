import { Component, ViewChild } from '@angular/core';
import { ApiService } from './services/api.service';
import { ReportService } from './services/report.service';
import { MatTableDataSource } from '@angular/material/table';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})



export class AppComponent {
  cities: any = {
    M: 'Los Mochis',
    N: 'Navojoa',
    O: 'Obregon'
  }

  @ViewChild(MatPaginator, { static: false })
  set paginator(value: MatPaginator) {
    if (this.dataSource) {
      this.dataSource.paginator = value;
    }
  }

  //Establece un Orden Utilizando Datos de la API
  @ViewChild(MatSort, { static: false })
  set sort(value: MatSort) {
    if (this.dataSource) {
      this.dataSource.sort = value;
    }
  }

  dataSource = new MatTableDataSource<any>();
  displayedColumns: string[] = [

    'src',
    'dst',
    'duration',
    'disposition',
    'calldate',
    "ciudad"
  ];
  title = 'webapp';

  results = false;
  calls: any = []


  fechaInicio: string = ''
  fechaFin: string = ''

  origen: string = '';
  destino: string = '';

  filtro: string = '';
  ciudad: string = '';
  estadoLlamada: string = '';
  estados = [
    { value: 'ANSWERED', status: 'Contestada' },
    { value: 'BUSY', status: 'Ocupado' },
    { value: 'NOT ANSWERED', status: 'Sin Respuesta' },
    { value: 'FAILED', status: 'Fallida' }
  ];
  ciudades = [
    { value: 'Los Mochis', name: 'Mochis' },
    { value: 'Navojoa', name: 'Navojoa' },
    { value: 'Obregon', name: 'Obregon' }
  ];

  constructor(private api: ApiService, private PDF: ReportService) { }

  ngOnInit(): void {
    this.buscar()
  }

  buscar() {
    // Llama al método buscar() de ApiService
    this.api.getCalls({
      src: this.isNull(this.origen), dst: this.isNull(this.destino), city: this.isNull(this.ciudad), status: this.isNull(this.estadoLlamada), d1: this.isNull(this.fechaInicio), d2: this.isNull(this.fechaFin)
    }).subscribe((data: any) => {
      this.results = true;
       this.dataSource.data=data;
    });
  }

  isNull(value: any) {
    return (value == '') ? null : value;
  }
  generarReporte() {
    Promise.all([this.PDF.exportAsPDF()])

}

}

import { Injectable } from '@angular/core';
import {  TextboxQuestion } from './question-textbox';
import { DropdownQuestion } from './question-dropdown';
import { of } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class QuestionService {
  // Simula a obtenção de dados de um recurso remoto
  getQuestions() {
    const questions = [
      new DropdownQuestion({
        key: 'brave',
        label: 'Bravery Rating',
        options: [
          {key: 'solid', value: 'Solid'},
          {key: 'great', value: 'Great'},
          {key: 'good', value: 'Good'},
          {key: 'unproven', value: 'Unproven'}
        ],
        order: 3
      }),
      new TextboxQuestion({
        key: 'firstName',
        label: 'First name',
        value: 'Bombasto',
        required: true,
        order: 1
      }),
      // outras perguntas
    ];

    return of(questions.sort((a, b) => a.order - b.order));
  }
}
